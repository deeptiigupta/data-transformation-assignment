import pandas as pd
import sqlite3
import os

def compare_catalogs(day1_csv, day2_csv, output_dir='output', key_column='product_id'):
    # Step 1: Load the CSVs
    df1 = pd.read_csv(day1_csv)
    df2 = pd.read_csv(day2_csv)

    # Step 2: Clean column names
    df1.columns = df1.columns.str.strip().str.lower()
    df2.columns = df2.columns.str.strip().str.lower()

    # Step 3: Load into SQLite in-memory database
    conn = sqlite3.connect(":memory:")
    df1.to_sql("products_day1", conn, index=False, if_exists="replace")
    df2.to_sql("products_day2", conn, index=False, if_exists="replace")

    # Step 4: Identify full row changes (added or removed)
    row_change_query = f"""
    SELECT * , 'REMOVED' AS change_type
    FROM products_day1
    WHERE product_id NOT IN (
        SELECT product_id FROM products_day2
    )

    UNION ALL

    -- Added rows: exist in Day2 but not in Day1
    SELECT *, 'ADDED' AS change_type
    FROM products_day2
    WHERE product_id NOT IN (
        SELECT product_id FROM products_day1
    )
    """
    row_changes_df = pd.read_sql_query(row_change_query, conn)
   

    # Step 5: Identify column-level changes
    key_column="product_id"
    non_key_columns = [col for col in df1.columns if col != key_column]

    select_clause = [f"d1.{key_column}"]
    where_clause = []

    for col in non_key_columns:
        select_clause.append(f"d1.{col} AS old_{col}")
        select_clause.append(f"d2.{col} AS new_{col}")
        where_clause.append(f"d1.{col} != d2.{col}")

    column_diff_query = f"""
    SELECT {', '.join(select_clause)}
    FROM products_day1 d1
    JOIN products_day2 d2 ON d1.{key_column} = d2.{key_column}
    WHERE {' OR '.join(where_clause)}
    """

    column_diffs_df = pd.read_sql_query(column_diff_query, conn)

    # Step 6: Flatten to row-per-column-change format
    flattened = []
    for _, row in column_diffs_df.iterrows():
        for col in non_key_columns:
            old_val = row[f'old_{col}']
            new_val = row[f'new_{col}']
            if old_val != new_val:
                flattened.append({
                    key_column: row[key_column],
                    'column_changed': col,
                    'old_value': old_val,
                    'new_value': new_val
                })
    column_change_df = pd.DataFrame(flattened)

    # Step 7: Save results

     # Directory Creation
    os.makedirs(output_dir, exist_ok=True)
    
    #Output file
    row_changes_df.to_csv(f"{output_dir}/row_changes.csv", index=False)
    column_change_df.to_csv(f"{output_dir}/column_level_changes.csv", index=False)
    print("Output saved.", output_dir)

compare_catalogs("products_day1.csv", "products_day2.csv")
