# Kaggle Learn - Data Visualization Lesson 2: Line Charts
# 学習日: 2025-07-21

import pandas as pd

# ===== Exercise 1 =====
# 問題: Load the data

# Path of the file to read
museum_filepath = "../input/museum_visitors.csv"

# Fill in the line below to read the file into a variable museum_data
museum_data = pd.read_csv(museum_filepath,index_col='Date', parse_dates=True)

# ===== Exercise 2 =====
# 問題: Review the data

# Fill in the line below: How many visitors did the Chinese American Museum
# receive in July 2018?
ca_museum_jul18 = museum_data.loc['2018-07-01','Chinese American Museum']

# Fill in the line below: In October 2018, how many more visitors did Avila
# Adobe receive than the Firehouse Museum?
avila_oct18 = museum_data.loc['2018-10-01','Avila Adobe'] - museum_data.loc['2018-10-01','Firehouse Museum']

# ===== Exercise 3 =====
# Assess seasonality

plt.figure(figsize=(9,6))
sns.lineplot(data=museum_data)

# ===== Exercise 4 =====
# Assess seasonality

# Part A
plt.figure(figsize = (9,6))
sns.lineplot(data=museum_data['Avila Adobe'])
plt.xlabel("Date")

# Part B
# in September-February (in LA, the fall and winter months), or
# in March-August (in LA, the spring and summer)?
# Using this information, when should the museum staff additional seasonal employees?

#A.夏季に多く従業員を雇うことで、メリットを得られます。



