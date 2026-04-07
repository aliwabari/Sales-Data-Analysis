import pandas as pd 
from scripts import analyze as az 

df= pd.read_csv("data/cleaned/SalesDataCleaned2.csv")

median_per_country= az.median_per_country(df)
median_per_category= az.median_per_category(df)
top_products = az.top_products(df)
top_categories= az.top_categories(df)


print(f"Median per Country\n{median_per_country}")
print(f"Median per category\n{median_per_category}")
print(f"Top Products\n{top_products}")
print(f"Top Categories\n{top_categories}")