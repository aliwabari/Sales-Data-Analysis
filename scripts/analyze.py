import numpy as np 
import pandas as pd 

def top_countries(df):
    return df.groupby(["Country"])["Total"].sum().sort_values(ascending=False)
def top_products (df):
    return df.groupby("Product")["Total"].sum().sort_values(ascending=False)

def top_categories (df):
    return df.groupby("Category")["Total"].sum().sort_values(ascending=False)

def sales_per_months(df):
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    return df.groupby(df["Order Date"].dt.to_period("M"))["Total"].sum()

def discount_effect (df):
    return df.groupby("Discount%")["Total"].sum().sort_values(ascending=False)

def customer_frequency(df):
    filtered_customers =df[df["Customer Name"] != "Unknown"]
    return filtered_customers.groupby("Customer Name")["Order_ID"].count().sort_values(ascending=False)
def get_aov(df):
    total_sales = df["Total"].sum()
    total_orders= df["Order_ID"].nunique()

    aov = round(total_sales / total_orders , 2) 

    return  aov