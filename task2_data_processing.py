import pandas as pd



# Task 1: Load JSON

df = pd.read_json("data/trends_20240115.json")



print("Loaded", len(df), "stories")





# Task 2: Clean the data



# 1. Remove duplicate post_id

df = df.drop_duplicates(subset="post_id")



print("After removing duplicates:", len(df))





# 2. Remove rows missing post_id, title or score

df = df.dropna(subset=["post_id", "title", "score"])



print("After removing nulls:", len(df))





# 3. Convert score and num_comments to integers

df["score"] = df["score"].astype(int)

df["num_comments"] = df["num_comments"].astype(int)





# 4. Remove low scores

df = df[df["score"] >= 5]



print("After removing low scores:", len(df))





# 5. Remove extra spaces from title

df["title"] = df["title"].str.strip()





# Task 3: Save CSV

df.to_csv("data/trends_clean.csv", index=False)



print("Saved", len(df), "rows to data/trends_clean.csv")





# Stories per category

print("Stories per category:")

print(df["category"].value_counts())