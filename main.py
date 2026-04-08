import pandas as pd 
from scripts import analyze as az 

df= pd.read_csv("data/cleaned/SalesDataCleaned2.csv")

top_countires= az.top_countries(df)
top_products = az.top_products(df)
top_categories= az.top_categories(df)
sales_per_months=az.sales_per_months(df)
discount_effect=az.discount_effect(df)
customer_frequency = az.customer_frequency(df)
aov = az.get_aov(df)

print(f"Top Products\n{top_products}")
print(f"Top Categories\n{top_categories}")
print(f"Top Countries\n{top_countires}")
print(f"Performance Over Months\n{sales_per_months}")
print(f"Discount Effect\n{discount_effect}")
print(f"Customer Frequency\n{customer_frequency}")
print(f"AOV\n{aov}")

