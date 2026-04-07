import numpy as np 
import pandas as pd 

def median_per_country(df):
    return df.groupby(["Country"])["Total"].median().sort_values(ascending=False)
def top_products (df):
    return df.groupby("Product")["Total"].sum().sort_values(ascending=False)

def top_categories (df):
    return df.groupby("Category")["Total"].sum().sort_values(ascending=False)
