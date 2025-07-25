# Kaggle Learn - Intermediate Machine Learning Lesson 2: Missing Values
# 学習日: 2025-07-22

import pandas as pd

# ===== Exercise 1 =====
# 問題: Preliminary investigation

# Fill in the line below: How many rows are in the training data?
num_rows = 1168

# Fill in the line below: How many columns in the training data
# have missing values?
num_cols_with_missing = 3

# Fill in the line below: How many missing entries are contained in
# all of the training data?
tot_missing = 276

# Since there are relatively few missing entries in the data (the column with the greatest percentage of missing values is missing less than 20% of its entries),
# we can expect that dropping columns is unlikely to yield good results. This is because we'd be throwing away a lot of valuable data, and so imputation will likely perform better.

# ===== Exercise 2 =====
# 問題: Drop columns with missing values

cols_with_missing = [col for col in X_train.columns
                    if X_train[col].isnull().any()]
reduced_X_train = X_train.drop(cols_with_missing, axis=1)
reduced_X_valid = X_valid.drop(cols_with_missing, axis=1)

# MAE17837.82570776256

# ===== Exercise 3 =====
# 問題: Imputation

my_imputer = SimpleImputer()
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))

# Fill in the lines below: imputation removed column names; put them back
imputed_X_train.columns = X_train.columns
imputed_X_valid.columns = X_valid.columns

# MAE18062.894611872147

# ===== Exercise 4 =====
# 問題: Generate test predictions

final_imputer = SimpleImputer(strategy ='median')

final_X_train = pd.DataFrame(final_imputer.fit_transform(X_train))
final_X_valid = pd.DataFrame(final_imputer.transform(X_valid))

final_X_train.columns = X_train.columns
final_X_valid.columns = X_valid.columns

# MAE17791.59899543379

