# Kaggle Learn - Data Visualization Lesson 1: Hello, Seaborn
# 学習日: 2025-07-20

import pandas as pd

# ===== Exercise 1 =====
# 問題: Explore the feedback system

one = 1

# ===== Exercise 2 =====
# 問題: Load the data

fifa_filepath = "../input/fifa.csv"

fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)

# ===== Exercise 3 =====
# Plot the data

# Set the width and height of the figure
plt.figure(figsize=(16,6))

# Line chart showing how FIFA rankings evolved over time
sns.lineplot(data=fifa_data)
