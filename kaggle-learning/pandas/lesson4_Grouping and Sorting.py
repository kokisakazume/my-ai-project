# Kaggle Learn - Pandas Lesson 4: Grouping and Sorting
# 学習日: 2025-07-18

import pandas as pd

# ===== Exercise 1 =====
# 問題: Who are the most common wine reviewers in the dataset?
# Create a Series whose index is the taster_twitter_handle category from the dataset,
# and whose values count how many reviews each person wrote..
reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()

# ===== Exercise 2 =====
# 問題: What is the best wine I can buy for a given amount of money?
# Create a Series whose index is wine prices and whose values is the maximum number of points a wine costing that much was given in a review.
# Sort the values by price, ascending (so that 4.0 dollars is at the top and 3300.0 dollars is at the bottom).
best_rating_per_price = reviews.groupby('price').points.max()

# ===== Exercise 3 =====
# 問題: What are the minimum and maximum prices for each variety of wine?
# Create a DataFrame whose index is the variety category from the dataset and whose values are the min and max values thereof.

price_extremes = reviews.groupby('variety').price.agg([min,max])

# ===== Exercise 4 =====
# 問題: What are the most expensive wine varieties?
# Create a variable sorted_varieties containing a copy of the dataframe from the previous question
# where varieties are sorted in descending order based on minimum price, then on maximum price (to break ties).

sorted_varieties = price_extremes.sort_values(by =['min','max'],ascending = False)

# ===== Exercise 5 =====
# 問題: Create a Series whose index is reviewers and whose values is the average review score given out by that reviewer.

reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()

# ===== Exercise 6 =====
# 問題: What combination of countries and varieties are most common?
# Create a Series whose index is a MultiIndexof {country, variety} pairs.
# For example, a pinot noir produced in the US should map to {"US", "Pinot Noir"}.
# Sort the values in the Series in descending order based on wine count.

country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending = False)