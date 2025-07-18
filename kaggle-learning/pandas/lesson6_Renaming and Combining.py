# Kaggle Learn - Pandas Lesson 6: Renaming and Combining
# 学習日: 2025-07-18

import pandas as pd

# ===== Exercise 1 =====
# 問題: region_1 and region_2 are pretty uninformative names for locale columns in the dataset.
# Create a copy of reviews with these columns renamed to region and locale, respectively.
renamed = reviews.rename(columns={'region_1':'region','region_2':'locale'})

# ===== Exercise 2 =====
# 問題: Set the index name in the dataset to wines.
reindexed = reviews.rename_axis("wines", axis=0)

# ===== Exercise 3 =====
# 問題: The Things on Reddit dataset includes product links from a selection of top-ranked forums ("subreddits") on reddit.com.
# Run the cell below to load a dataframe of products mentioned on the /r/gaming subreddit and another dataframe for products mentioned on the r//movies subreddit.

combined_products = pd.concat([gaming_products,movie_products])

# ===== Exercise 4 =====
# 問題: The Powerlifting Database dataset on Kaggle includes one CSV table for powerlifting meets
# and a separate one for powerlifting competitors. Run the cell below to load these datasets into dataframes:

powerlifting_combined = powerlifting_meets.set_index('MeetID').join(powerlifting_competitors.set_index('MeetID'))