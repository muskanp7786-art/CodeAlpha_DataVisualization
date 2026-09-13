import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("books_dataset.csv")

# Convert Price into numeric value
df["Price"] = df["Price"].str.replace("£", "", regex=False)
df["Price"] = df["Price"].str.replace("Â", "", regex=False)
df["Price"] = df["Price"].astype(float)

# -------------------------------
# 1. Price Distribution
# -------------------------------

plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=8)

plt.xlabel("Book Price")
plt.ylabel("Number of Books")
plt.title("Distribution of Book Prices")

plt.tight_layout()
plt.savefig("visual_price_distribution.png")
plt.close()


# -------------------------------
# 2. Rating-wise Number of Books
# -------------------------------

plt.figure(figsize=(8, 5))
df["Rating"].value_counts().plot(kind="bar")

plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.title("Number of Books by Rating")

plt.tight_layout()
plt.savefig("visual_rating_distribution.png")
plt.close()


# -------------------------------
# 3. Top 10 Expensive Books
# -------------------------------

top_books = df.sort_values("Price", ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.barh(top_books["Title"], top_books["Price"])

plt.xlabel("Price")
plt.ylabel("Book Title")
plt.title("Top 10 Most Expensive Books")
plt.gca().invert_yaxis()

plt.tight_layout()
plt.savefig("top_10_expensive_books.png")
plt.close()


# -------------------------------
# 4. Price vs Rating
# -------------------------------

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating_Number"] = df["Rating"].map(rating_map)

plt.figure(figsize=(8, 5))
plt.scatter(df["Rating_Number"], df["Price"])

plt.xlabel("Rating")
plt.ylabel("Book Price")
plt.title("Book Price vs Rating")

plt.tight_layout()
plt.savefig("visual_price_vs_rating.png")
plt.close()


print("===================================")
print("DATA VISUALIZATION COMPLETED!")
print("===================================")
print("4 visualization graphs created successfully.")