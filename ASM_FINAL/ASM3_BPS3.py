import pandas as pd

df = pd.read_csv("Dữ liệu về sản phẩm và giá.txt")
df["ProductName"] = df["ProductName"].fillna("No Product")

print(df)
df.to_csv("Dữ liệu về sản phẩm và giá.txt", index=False)