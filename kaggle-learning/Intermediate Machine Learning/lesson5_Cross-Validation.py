# Kaggle Learn - Intermediate Machine Learning Lesson 5: Cross-Validation
# 学習日: 2025-07-27

import pandas as pd

# ===== Exercise 1 =====
# 問題: Write a useful function

def get_score(n_estimators):
    my_pipeline = Pipeline(steps=[
        ('preprocessor', SimpleImputer()),
        ('model', RandomForestRegressor(n_estimators, random_state=0))
    ])
    scores = -1 * cross_val_score(my_pipeline, X, y,
                                  cv=3,
                                  scoring='neg_mean_absolute_error')
    return scores.mean()
    # Replace this body with your own code
    pass


# ===== Exercise 2 =====
# 問題: Test different parameter values

results = {}
for i in range(1,9):
    results[50*i] = get_score(50*i)

# ===== Exercise 3 =====
# 問題: Find the best parameter value

n_estimators_best = 200
