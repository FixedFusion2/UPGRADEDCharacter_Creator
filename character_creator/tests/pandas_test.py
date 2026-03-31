import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("character_creator\docs\data.csv")

# Print the entire DataFrame (useful for small datasets)
# print(df.to_string()) 

# Print the first 5 rows to quickly analyze the data (recommended for large files)
print(df.head())