# Kaggle Learn - Data Visualization Lesson 3: Bar Charts and Heatmaps
# 学習日: 2025-07-21

import pandas as pd

# ===== Exercise 1 =====
# 問題: Load the data¶

# Path of the file to read
ign_filepath = "../input/ign_scores.csv"

# Fill in the line below to read the file into a variable ign_data
ign_data = pd.read_csv(ign_filepath,index_col='Platform')

# ===== Exercise 2 =====
# 問題: Review the data

# Fill in the line below: What is the highest average score received by PC games,
# for any genre?
high_score = ign_data.loc['PC'].max()

# Fill in the line below: On the Playstation Vita platform, which genre has the
# lowest average score? Please provide the name of the column, and put your answer
# in single quotes (e.g., 'Action', 'Adventure', 'Fighting', etc.)
worst_genre = ign_data.loc['PlayStation Vita'].idxmin()

# ===== Exercise 3 =====
# Which platform is best?

plt.figure(figsize=(9,6))
sns.barplot(x=ign_data['Racing'], y=ign_data.index)

# ===== Exercise 4 =====
# All possible combinations!

plt.figure(figsize=(10,10))

sns.heatmap(ign_data,annot = True)



