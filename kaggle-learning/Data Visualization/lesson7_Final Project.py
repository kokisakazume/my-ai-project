# Kaggle Learn - Data Visualization Lesson 7: Final Project
# 学習日: 2025-07-22

# Visualize the data

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(9,6))
sns.regplot(x = my_data['Salt_Intake'],y = my_data['BMI'])

# 高血圧リスク予測データセットより、塩分摂取量とBMIに若干の正の相関があることがわかった。