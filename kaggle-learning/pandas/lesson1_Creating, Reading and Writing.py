# Kaggle Learn - Pandas Lesson 1: Creating, Reading and Writing
# 学習日: 2025-07-16

import pandas as pd

# ===== レッスン内容 =====
# DataFrameの基本的な作成方法

# ===== Exercise 1 =====
# 問題: create a DataFrame
fruits = pd.DataFrame({'Apples': [30], 'Bananas': [21]})

# ===== Exercise 2 =====
# 問題: Create a dataframe with index
fruits = pd.DataFrame([[35, 21],[41,34]], columns=['Apples', 'Bananas'],index=['2017 Sales', '2018 Sales'])

# ===== Exercise 3 =====
# 問題: Create a variable ingredients with a Series

drink = ['4 cups','1 cups', '2 large' , '1 can']
items = ['Flour','Milk', 'Eggs', 'Spam']
cook = pd.Series(drink,index = items , name='Dinner')

# ===== Exercise 4 =====
# 問題: Read the following csv dataset of wine reviews into a DataFrame called reviews

reviews = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv', index_col=0)

# ===== Exercise 5 =====
# 問題: Run the cell below to create and display a DataFrame called animals:

animals.to_csv("animal.csv")
