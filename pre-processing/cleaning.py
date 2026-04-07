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
df=df[df["Total"] > 0 ]
df=df[df["Unit Price"] > 0 ]
df=df[df["Quantity"] > 0 ]
df["Total"] = df["Quantity"] * df["Unit Price"]
df["Discounted_Total"] = df["Total"] - (df["Total"] * (df["Discount%"] / 100))
df["Order Date"] = pd.to_datetime(df["Order Date"]   , errors="coerce")


df["Category"]= df["Category"].str.lower()
category_mapping = {
    'electronics': 'electronics',
    'accessories': 'accessories',
    'elec.': 'electronics',  # Handle abbreviation
    'acc.': 'accessories',   # Handle abbreviation
    'acessories': 'accessories',  # Handle typo
    'accessory': 'accessories',   # Handle typo
    'electronic': 'electronics',  # Handle typo
    'electonics':"electronics"
}
df['Category'] = df['Category'].replace(category_mapping)
df['Product'] = df['Product'].str.lower()
df['Product'] = df['Product'].str.strip()

df.to_csv("Data/cleaned/SalesDataCleaned2.csv" , index=False)
