import pandas as pd 
# exploaring python file 
df = pd.read_excel("data/raw/SalesData.xlsx")
print(df.dtypes())
print(f"head of df => \n{df.head()}")
print(f"Data Overview => \n{df.describe()} ")
print(f"Length of data => \n{len(df)}")
print(f"Missing values => \n{df.isnull().sum()}")
print(f"Duplicated values => \n{df.duplicated().sum()}")
