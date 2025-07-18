# Kaggle Learn - Intro to Machine Learning Lesson 2: Explore Your Data
# 学習日: 2025-07-19

import pandas as pd

# ===== Exercise 1 =====
# 問題: Read the Iowa data file into a Pandas DataFrame called home_data.
home_data = pd.read_csv(iowa_file_path)

# ===== Exercise 2 =====
# 問題: Use the command you learned to view summary statistics of the data. Then fill in variables to answer the following questions

# What is the average lot size (rounded to nearest integer)?
avg_lot_size = home_data['LotArea'].mean().round()

# As of today, how old is the newest home (current year - the date in which it was built)
newest_home_age = 2025 - home_data['YrSold'].max()

