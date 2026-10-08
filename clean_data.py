import pandas as pd

df = pd.read_csv("books_raw.csv")

# Price: "£51.77" -> 51.77
df["Price"] = df["Price"].str.replace(r"[^\d.]", "", regex=True).astype(float)

# Rating: "Three" -> 3
rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
df["Rating"] = df["Rating"].map(rating_map)

# Availability: keep as True/False
df["In_Stock"] = df["Availability"].str.contains("In stock")
df = df.drop(columns=["Availability"])

# Remove duplicates and missing values
df = df.drop_duplicates()
df = df.dropna()

print(df.info())
print(df.describe())

df.to_csv("books_clean.csv", index=False)
df.to_excel("books_clean.xlsx", index=False)
print("Clean dataset saved!")