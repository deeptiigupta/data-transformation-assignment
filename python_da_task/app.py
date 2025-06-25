import pandas as pd
from datetime import datetime


df = pd.read_csv("raw_sales.csv")

#function for data transformation
def to_int(val, default=0):
    try:
        return abs(int(float(str(val).strip('"').strip())) )
    except (ValueError, TypeError):
        return default
    

def to_float(val):
    try:
        val = str(val).strip('"').strip()
        return round(float(val), 2) if val else 0.00
    except:
        return 0.00

def to_date(val):
    try:
        val = str(val).strip('"').strip()
        return pd.to_datetime(val, errors='coerce', dayfirst=True)
    except:
        return pd.NaT


df['order_id'] = df['order_id'].apply(to_int)
df['product_id'] = df['product_id'].apply(to_int)
df['quantity'] = df['quantity'].apply(to_int)
df['price_per_unit'] = df['price_per_unit'].apply(to_float)
df['order_date'] = df['order_date'].apply(to_date)

#Fuction to calculate total_price
def compute_total_price(row):
    return row['quantity'] * row['price_per_unit']

df['total_price'] = df.apply(compute_total_price, axis=1)

#To Save file
df.to_csv("cleaned_sales.csv", index=False)
