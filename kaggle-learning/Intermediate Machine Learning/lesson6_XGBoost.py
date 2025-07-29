# Kaggle Learn - Intermediate Machine Learning Lesson 6: XGBoost
# 学習日: 2025-07-28

import pandas as pd

# ===== Exercise 1 =====
# 問題: Build model

# Define the model
my_model_1 = XGBRegressor(random_state = 0)

# Fit the model
my_model_1.fit(X_train, y_train)

from sklearn.metrics import mean_absolute_error

predictions_1 = my_model_1.predict(X_valid)

mae_1 = mean_absolute_error(predictions_1,y_valid)

# MAE 18161.82412510702

# ===== Exercise 2 =====
# 問題: Improve the model

# Define the model
my_model_2 = XGBRegressor(n_estimators=1000, learning_rate=0.05)

# Fit the model
my_model_2.fit(X_train,y_train) # Your code here

# Get predictions
predictions_2 =  my_model_2.predict(X_valid)

# Calculate MAE
mae_2 = mean_absolute_error(predictions_2, y_valid)

#MAE 17224.27947078339

# ===== Exercise 3 =====
# 問題: Break the model

# Define the model
my_model_3 = XGBRegressor(n_estimators=1)

# Fit the model
my_model_3.fit(X_train,y_train) # Your code here

# Get predictions
predictions_3 = my_model_3.predict(X_valid)

# Calculate MAE
mae_3 = mean_absolute_error(predictions_3, y_valid)

# MAE 42678.815550085616
