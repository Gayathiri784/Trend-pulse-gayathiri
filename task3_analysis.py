import pandas as pd
import numpy as np

# 1. Load the clean CSV
df = pd.read_csv("data/trends_clean.csv")

print("Loaded data:", df.shape)

# Print first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Average score and comments
print("\nAverage score:", df["score"].mean())
print("Average comments:", df["num_comments"].mean())


# 2. NumPy Analysis

scores = df["score"].to_numpy()

print("\n--- NumPy Stats ---")

print("Mean score:", np.mean(scores))
print("Median score:", np.median(scores))
print("Std deviation:", np.std(scores))

print("Max score:", np.max(scores))
print("Min score:", np.min(scores))


# Category with the most stories
category_counts = df["category"].value_counts()
most_category = category_counts.idxmax()
most_category_count = category_counts.max()

print("\nMost stories in:", most_category,
      "(", most_category_count, "stories)")


# Story with the most comments
max_comments_index = df["num_comments"].idxmax()

print("\nMost commented story:",
      df.loc[max_comments_index, "title"],
      "-",
      df.loc[max_comments_index, "num_comments"],
      "comments")


# 3. Add New Columns

average_score = df["score"].mean()

df["engagement"] = df["num_comments"] / (df["score"] + 1)

df["is_popular"] = df["score"] > average_score


# 4. Save the result

df.to_csv("data/trends_analysed.csv", index=False)

print("\nSaved analysed data to data/trends_analysed.csv")