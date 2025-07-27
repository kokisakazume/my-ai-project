# Kaggle Learn - Intermediate Machine Learning Lesson 4: Pipelines
# 学習日: 2025-07-26

import pandas as pd

# ===== Exercise 1 =====
# 問題: Improve the performance

numerical_transformer = SimpleImputer(strategy='constant')

# Preprocessing for categorical data
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])


# Bundle preprocessing for numerical and categorical data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

# Define model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# MAE 17681.395445205482

# ===== Exercise 2 =====
# 問題: Generate test predictions

preds_test = my_pipeline.predict(X_test)
