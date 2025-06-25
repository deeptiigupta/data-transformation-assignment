# data-transformation-assignment 

Task 1: Compare Product Catalogs Over Two Days

*What it does:
This script compares two versions of a product catalog (products_day1.csv and products_day2.csv) to:

i.Identify products that were added or removed
ii.Detect column-level changes for existing products (e.g., price, stock)

*Logic behind the code:
i.Reads both CSV files using pandas.
ii.Loads the data into an in-memory SQL database using sqlite3.
iii.Runs SQL queries to:
    Compare entire rows and flag additions/removals
    Compare column values (name, category, price, stock) for matching product IDs

Outputs two files:
i.row_changes.csv: shows full rows that were added or removed
ii. column_level_changes.csv: shows what specific values changed

Name of output files:
i.output/row_changes.csv
ii.output/column_level_changes.csv


-----------------------------------------------------------------------------------------------------------------------------------------

Task 2: Clean Messy Order Data
* What it does:
  Takes a messy order data file with:
      Bad quotes (like "")
      Mixed data types (strings instead of numbers)
      Inconsistent date formats
  And cleans it up into a proper, usable CSV.
  
*Logic behind the code:
i.Parses and normalizes values like quantity and price_per_unit
ii.Converts all dates into YYYY-MM-DD format
iii. Leaves missing values blank

Name of output files:
cleaned_sales.csv
