# Section 6: Data Analysis and Visualization

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned quotes data
df = pd.read_csv("quotes_cleaned.csv")

# --- Part 1: Bar chart of top 10 quoted authors ---

# Count quotes by author and get top 10
author_counts = df["Author"].value_counts().head(10)

# Plot horizontal bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x=author_counts.values, y=author_counts.index, palette="Blues_r")
plt.title("Top 10 Quoted Authors")
plt.xlabel("Number of Quotes")
plt.ylabel("Author")
plt.tight_layout()
plt.show()

# --- Part 2: Time series visualization of quote frequency ---

# Simulate dates for each quote (replace with real scraped dates if available)
df["Date"] = pd.date_range(start="2024-01-01", periods=len(df), freq="D")

# Group quotes by week
weekly_counts = df.groupby(pd.Grouper(key="Date", freq="W")).size()

# Plot weekly frequency as a line chart
plt.figure(figsize=(10, 5))
sns.lineplot(x=weekly_counts.index, y=weekly_counts.values, marker="o")
plt.title("Weekly Quote Frequency")
plt.xlabel("Date")
plt.ylabel("Number of Quotes")
plt.tight_layout()
plt.show()

# --- Part 3: Simple dashboard combining both charts ---

fig, axes = plt.subplots(2, 1, figsize=(12, 10))

# Bar chart: top authors
sns.barplot(x=author_counts.values, y=author_counts.index, ax=axes[0], palette="Greens_r")
axes[0].set_title("Top 10 Quoted Authors")
axes[0].set_xlabel("Number of Quotes")
axes[0].set_ylabel("Author")

# Line chart: weekly frequency
sns.lineplot(x=weekly_counts.index, y=weekly_counts.values, ax=axes[1], marker="o")
axes[1].set_title("Quote Frequency Over Time")
axes[1].set_xlabel("Date")
axes[1].set_ylabel("Number of Quotes")

plt.tight_layout()
plt.show()

# --- Bonus: Save figures as images ---

# Uncomment the lines below to save the figures
# plt.figure(figsize=(10, 6))
# sns.barplot(x=author_counts.values, y=author_counts.index, palette="Blues_r")
# plt.title("Top 10 Quoted Authors")
# plt.xlabel("Number of Quotes")
# plt.ylabel("Author")
# plt.tight_layout()
# plt.savefig("top_authors.png")

# plt.figure(figsize=(10, 5))
# sns.lineplot(x=weekly_counts.index, y=weekly_counts.values, marker="o")
# plt.title("Weekly Quote Frequency")
# plt.xlabel("Date")
# plt.ylabel("Number of Quotes")
# plt.tight_layout()
# plt.savefig("weekly_frequency.png")
