# Kaggle Learn - Intro to Machine Learning Lesson 7: Machine Learning Competitions
# 学習日: 2025-07-20

import pandas as pd

# ===== Exercise 1 =====
# 問題: Machine Learning Competitions

# To improve accuracy, create a new Random Forest model which you will train on all training data

rf_model_on_full_data = RandomForestRegressor()

# fit rf_model_on_full_data on all data from the training data

rf_model_on_full_data.fit(X, y)

# path to file you will use for predictions
test_data_path = '../input/test.csv'

# read test data file using pandas
test_data = pd.read_csv(test_data_path)

# create test_X which comes from test_data but includes only the columns you used for prediction.
# The list of columns is stored in a variable called features
test_X = test_data[features]

# make predictions which we will submit.
test_preds = rf_model_on_full_data.predict(test_X)


Housing Prices Competition for Kaggle Learn Users
leaderboard:3883  2025/7/20
Score: 21100.16255

