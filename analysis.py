import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("books_clean.csv")

print("Average price:", round(df["Price"].mean(), 2))
print("Most expensive:", df.loc[df["Price"].idxmax(), "Title"])
print("Cheapest:", df.loc[df["Price"].idxmin(), "Title"])
print("\nBooks per rating:\n", df["Rating"].value_counts().sort_index())

# Chart 1: books per rating
df["Rating"].value_counts().sort_index().plot(kind="bar")
plt.title("Number of Books per Rating")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.savefig("rating_chart.png")
plt.show()

# Chart 2: price distribution
df["Price"].plot(kind="hist", bins=20)
plt.title("Price Distribution")
plt.xlabel("Price (£)")
plt.savefig("price_chart.png")
plt.show()   