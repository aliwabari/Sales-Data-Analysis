import pandas as pd 

df  = pd.read_excel("data/raw/SalesData.xlsx")
df.columns = df.columns.str.strip()
df = df.drop_duplicates()
df = df.dropna(subset=["Order_ID" , "Product" , "Category" , "Unit Price" , "Order Date" ,"Ship Date","City","Payment Method","Status"]) 
df["Customer Name"] = df["Customer Name"].fillna("Unknown"  )
df["Email"] = df["Email"].fillna("Not Provided"  )
df["Country"]= df["Country"].fillna(df["Country"].mode()[0] )
df["Region"]= df["Region"].fillna(df["Region"].mode()[0] )

df["Discount%"] = pd.to_numeric(df["Discount%"] , errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"] , errors='coerce')
df["Unit Price"]=pd.to_numeric(df["Unit Price"] , errors='coerce')
df["Total"] = pd.to_numeric(df["Total"] , errors='coerce')

df["Total"] = df["Quantity"] * df["Unit Price"]
df["Discounted_Total"] = df["Total"] - (df["Total"] * (df["Discount%"] / 100))

df.to_csv("Data/cleaned/SalesDataCleaned.csv" , index=False)
