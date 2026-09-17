import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the analysed data from Task 3
df = pd.read_csv("data/trends_analysed.csv")

# Create outputs folder if it does not exist
os.makedirs("outputs", exist_ok=True)


# =========================================================
# CHART 1 - TOP 10 STORIES BY SCORE
# =========================================================

# Select the 10 stories with the highest scores
top10 = df.nlargest(10, "score").copy()

# Shorten long story titles
top10["short_title"] = top10["title"].astype(str).apply(
    lambda x: x[:50] + "..." if len(x) > 50 else x
)

plt.figure(figsize=(10, 6))

plt.barh(top10["short_title"], top10["score"])

plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")

# Show highest score at the top
plt.gca().invert_yaxis()

plt.tight_layout()

# Save before showing
plt.savefig("outputs/chart1_top_stories.png")

plt.show()
plt.close()


# =========================================================
# CHART 2 - STORIES PER CATEGORY
# =========================================================

# Count the number of stories in each category
category_counts = df["category"].value_counts()

plt.figure(figsize=(9, 6))

# Give each category a different colour
plt.bar(
    category_counts.index,
    category_counts.values,
    color=plt.cm.tab10(range(len(category_counts)))
)

plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.xticks(rotation=30)

plt.tight_layout()

# Save before showing
plt.savefig("outputs/chart2_categories.png")

plt.show()
plt.close()


# =========================================================
# CHART 3 - SCORE VS COMMENTS
# =========================================================

plt.figure(figsize=(10, 6))

# Separate popular and non-popular stories
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

# Plot non-popular stories
plt.scatter(
    not_popular["score"],
    not_popular["num_comments"],
    label="Non-Popular",
    alpha=0.6
)

# Plot popular stories
plt.scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular",
    alpha=0.6
)

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")

plt.legend()

plt.tight_layout()

# Save before showing
plt.savefig("outputs/chart3_scatter.png")

plt.show()
plt.close()


# =========================================================
# BONUS - DASHBOARD
# =========================================================

plt.figure(figsize=(16, 10))


# -------------------------
# Dashboard Chart 1
# -------------------------
plt.subplot(2, 2, 1)

plt.barh(top10["short_title"], top10["score"])

plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")

plt.gca().invert_yaxis()


# -------------------------
# Dashboard Chart 2
# -------------------------
plt.subplot(2, 2, 2)

plt.bar(
    category_counts.index,
    category_counts.values,
    color=plt.cm.tab10(range(len(category_counts)))
)

plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.xticks(rotation=30)


# -------------------------
# Dashboard Chart 3
# -------------------------
plt.subplot(2, 1, 2)

plt.scatter(
    not_popular["score"],
    not_popular["num_comments"],
    label="Non-Popular",
    alpha=0.6
)

plt.scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular",
    alpha=0.6
)

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")

plt.legend()


# Overall dashboard title
plt.suptitle("TrendPulse Dashboard", fontsize=18)

plt.tight_layout()

# Save dashboard
plt.savefig("outputs/dashboard.png")

plt.show()
plt.close()


print("=================================")
print("Task 4 completed successfully!")
print("=================================")
print("Created files:")
print("1. outputs/chart1_top_stories.png")
print("2. outputs/chart2_categories.png")
print("3. outputs/chart3_scatter.png")
print("4. outputs/dashboard.png")