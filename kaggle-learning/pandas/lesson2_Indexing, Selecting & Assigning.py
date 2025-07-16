# Kaggle Learn - Pandas Lesson 2: Indexing, Selecting & Assigning
# 学習日: 2025-07-17

import pandas as pd

# ===== Exercise 1 =====
# 問題: Select the description column from reviews and assign the result to the variable desc.
desc = reviews["description"]

# ===== Exercise 2 =====
# 問題: Select the first value from the description column of reviews, assigning it to variable first_description.
first_description = reviews["description"][0]

# ===== Exercise 3 =====
# 問題: Select the first row of data (the first record) from reviews, assigning it to the variable first_row.

first_row = reviews.iloc[0]

# ===== Exercise 4 =====
# 問題: Select the first 10 values from the description column in reviews,
#       assigning the result to variable first_descriptions.s

first_descriptions = reviews.description.iloc[:10]

# ===== Exercise 5 =====
# 問題: Select the records with index labels 1, 2, 3, 5, and 8, assigning the result to the variable sample_reviews.

sample_reviews = reviews.iloc[index]
index =[1,2,3,5,8]
