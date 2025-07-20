# Kaggle Learn - Intro to Machine Learning Lesson 4: Model Validation
# 学習日: 2025-07-20

import pandas as pd

# ===== Exercise 1 =====
# 問題: Split Your Data

# Import the train_test_split function and uncomment
from sklearn.model_selection import train_test_split

# fill in and uncomment
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

# ===== Exercise 2 =====
# 問題: Specify and Fit the Model

# Specify the model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit iowa_model with the training data.
iowa_model.fit(train_X,train_y)

# ===== Exercise 3 =====
# 問題: Make Predictions with Validation data.

val_predictions = iowa_model.predict(val_X)

# ===== Exercise 4 =====
# 問題: Calculate the Mean Absolute Error in Validation Data

val_mae = mean_absolute_error(val_y, val_predictions)
