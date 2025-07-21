# Kaggle Learn - Data Visualization Lesson 5: Distributions
# 学習日: 2025-07-21

import pandas as pd

# ===== Exercise 1 =====
# 問題: Load the data¶

# Path of the files to read
cancer_filepath = "../input/cancer.csv"

# Fill in the line below to read the file into a variable cancer_data
cancer_data = pd.read_csv(cancer_filepath,index_col = 'Id')

# ===== Exercise 2 =====
# 問題: Review the data

# Fill in the line below: In the first five rows of the data, what is the
# largest value for 'Perimeter (mean)'?
max_perim = cancer_data.head().loc[:,'Perimeter (mean)'].max()

# Fill in the line below: What is the value for 'Radius (mean)' for the tumor with Id 8510824?
mean_radius = cancer_data.loc[8510824,'Radius (mean)']

subset2 = candy_data.loc[[2,4]]
more_sugar =  subset2.loc[subset2['sugarpercent'].idxmax(),'competitorname']

# ===== Exercise 3 =====
# Investigating differences

sns.histplot(data = cancer_data,x ='Area (mean)',hue = 'Diagnosis')

# ===== Exercise 4 =====
#  A very useful column

sns.kdeplot(data=cancer_data, x='Area (mean)', hue='Diagnosis')

