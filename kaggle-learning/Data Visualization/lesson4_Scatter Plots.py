# Kaggle Learn - Data Visualization Lesson 4: Scatter Plots
# 学習日: 2025-07-21

import pandas as pd

# ===== Exercise 1 =====
# 問題: Load the data¶

# Path of the file to read
candy_filepath = "../input/candy.csv"

# Fill in the line below to read the file into a variable candy_data
candy_data = pd.read_csv(candy_filepath,index_col = 'id')

# ===== Exercise 2 =====
# 問題: Review the data

# Fill in the line below: Which candy was more popular with survey respondents:
# '3 Musketeers' or 'Almond Joy'?  (Please enclose your answer in single quotes.)

subset = candy_data.loc[[1,3]]
more_popular =  subset.loc[subset['winpercent'].idxmax(),'competitorname']

# Fill in the line below: Which candy has higher sugar content: 'Air Heads'
# or 'Baby Ruth'? (Please enclose your answer in single quotes.)

subset2 = candy_data.loc[[2,4]]
more_sugar =  subset2.loc[subset2['sugarpercent'].idxmax(),'competitorname']

# ===== Exercise 3 =====
# The role of sugar

sns.scatterplot(x = candy_data['sugarpercent'],y = candy_data['winpercent'])

# ===== Exercise 4 =====
#  Take a closer look

sns.regplot(x = candy_data['sugarpercent'],y = candy_data['winpercent'])

# ===== Exercise 5 =====
#  Chocolate!

sns.scatterplot(x = candy_data['sugarpercent'],y = candy_data['winpercent'],hue = candy_data['chocolate'])

# ===== Exercise 6 =====
#  Investigate chocolate

sns.lmplot(x = 'sugarpercent',y = 'winpercent',hue = 'chocolate',data = candy_data)

# ===== Exercise 7 =====
#  Everybody loves chocolate.

sns.swarmplot(x = candy_data['chocolate'],y = candy_data['winpercent'])

