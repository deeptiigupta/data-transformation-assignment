# data-transformation-assignment <br>


PREREQUISITE- Install pandas
command- pip3 install pandas

Task 1: Compare Product Catalogs Over Two Days <br>

*What it does:<br>
This script compares two versions of a product catalog (products_day1.csv and products_day2.csv) to: <br>

i.Identify products that were added or removed <br>
ii.Detect column-level changes for existing products (e.g., price, stock) <br>

*Logic behind the code:<br>
i.Reads both CSV files using pandas. <br>
ii.Loads the data into an in-memory SQL database using sqlite3.<br>
iii.Runs SQL queries to:<br>
    Compare entire rows and flag additions/removals<br>
    Compare column values (name, category, price, stock) for matching product IDs<br>

Outputs two files: <br>
i.row_changes.csv: shows full rows that were added or removed<br>
ii. column_level_changes.csv: shows what specific values changed<br>

Name of output files:<br>
i.output/row_changes.csv<br>
ii.output/column_level_changes.csv<br>


-----------------------------------------------------------------------------------------------------------------------------------------

Task 2: Clean Messy Order Data <br>
* What it does:<br>
  Takes a messy order data file with:<br>
      Bad quotes (like "")<br>
      Mixed data types (strings instead of numbers)<br>
      Inconsistent date formats<br>
  And cleans it up into a proper, usable CSV.<br>
  
*Logic behind the code:<br>
i.Parses and normalizes values like quantity and price_per_unit <br>
ii.Converts all dates into YYYY-MM-DD format<br>
iii. Leaves missing values blank<br>

Name of output files:<br>
cleaned_sales.csv<br>
