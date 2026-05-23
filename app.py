import pandas as pd

df = pd.read_csv("Teen_Mental_Health_Dataset.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())