# Kaggle Learn - Intro to Machine Learning Lesson 3: Your First Machine Learning Model
# 学習日: 2025-07-19

import pandas as pd

# ===== Exercise 1 =====
# 問題: Select the target variable, which corresponds to the sales price.
# Save this to a new variable called y. You'll need to print a list of the columns to find the name of the column you need.
y = home_data.SalePrice

# ===== Exercise 2 =====
# 問題: Now you will create a DataFrame called X holding the predictive features.

# Create the list of features below
feature_names = ['LotArea','YearBuilt','1stFlrSF','2ndFlrSF','FullBath','BedroomAbvGr','TotRmsAbvGrd']

# Select data corresponding to features in feature_names
X = home_data[feature_names]

# As of today, how old is the newest home (current year - the date in which it was built)
newest_home_age = 2025 - home_data['YrSold'].max()

# ===== Exercise 3 =====
# 問題: Create a DecisionTreeRegressor and save it iowa_model.
# Ensure you've done the relevant import from sklearn to run this command.
#
# Then fit the model you just created using the data in X and y that you saved above.

from sklearn.tree import DecisionTreeRegressor
#specify the model.
#For model reproducibility, set a numeric value for random_state when specifying the model

iowa_model = DecisionTreeRegressor(random_state=1)

# Fit the model
iowa_model.fit(X, y)

# ===== Exercise 3 =====
# 問題: Make predictions with the model's predict command using X as the data. Save the results to a variable called predictions.

predictions = iowa_model.predict(X)
