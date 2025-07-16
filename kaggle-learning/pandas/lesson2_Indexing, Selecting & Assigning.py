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
# assigning the result to variable first_descriptions.s

first_descriptions = reviews.description.iloc[:10]

# ===== Exercise 5 =====
# 問題: Select the records with index labels 1, 2, 3, 5, and 8, assigning the result to the variable sample_reviews.

sample_reviews = reviews.iloc[index]
index =[1,2,3,5,8]

# ===== Exercise 6 =====
# 問題: Create a variable df containing the country, province, region_1,
# and region_2 columns of the records with the index labels 0, 1, 10, and 100.
# In other words, generate the following DataFrame:

col = ["country","province","region_1","region_2"]
index = [0,1,10,100]
df = reviews.loc[index, col]

# ===== Exercise 7 =====
# 問題: Create a variable df containing the country and variety columns of the first 100 records.

col = ["country", "variety"]
df = reviews.loc[:99,col]

# ===== Exercise 8 =====
# 問題: Create a DataFrame italian_wines containing reviews of wines made in Italy.

italian_wines = reviews.loc[(reviews.country == 'Italy')]

# ===== Exercise 9 =====
# 問題: Create a DataFrame top_oceania_wines
# containing all reviews with at least 95 points (out of 100) for wines from Australia or New Zealand.

top_oceania_wines = reviews.loc[reviews.country.isin(['Australia', 'New Zealand']) & (reviews.points >= 95)]