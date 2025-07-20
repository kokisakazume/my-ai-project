# Kaggle Learn - Intro to Machine Learning Lesson 6: Random Forests
# 学習日: 2025-07-20

import pandas as pd

# ===== Exercise 1 =====
# 問題: Use a Random Forest

from sklearn.ensemble import RandomForestRegressor

# Define the model. Set random_state to 1
rf_model = RandomForestRegressor(random_state=1)

# fit your model
rf_model.fit(train_X, train_y)

# Calculate the mean absolute error of your Random Forest model on the validation data
rf_val_predictions = rf_model.predict(val_X)
rf_val_mae = mean_absolute_error(rf_val_predictions, val_y)

print("Validation MAE for Random Forest Model: {}".format(rf_val_mae))


