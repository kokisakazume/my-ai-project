# Kaggle Learn - Intermediate Machine Learning Lesson 1: Introduction
# 学習日: 2025-07-22

import pandas as pd
from sklearn.model_selection import train_test_split

# Read the data
X_full = pd.read_csv('../input/train.csv', index_col='Id')
X_test_full = pd.read_csv('../input/test.csv', index_col='Id')

# Obtain target and predictors
y = X_full.SalePrice
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = X_full[features].copy()
X_test = X_test_full[features].copy()

X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.7, test_size=0.3,
                                                      random_state=0)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

model = RandomForestRegressor(n_estimators=100, criterion='absolute_error', random_state=0)
model.fit(X_train, y_train)
y_pred = model.predict(X_valid)

mean_absolute_error(y_valid, y_pred)

# 例よりも、数値の改善に成功
# 23528→22582.4653196347