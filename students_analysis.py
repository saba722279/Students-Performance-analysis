import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("students_performance.csv")

print("First 5 rows:")
print(data.head())

print("Information:")
print(data.info())

print("Statistics:")
print(data.describe())

average_scores = data[['Math_Score', 'English_Score', 'Science_Score']].mean()
print("Average Scores:")
print(average_scores)

average_scores.plot(kind='bar')
plt.title("Average Scores of Students")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.show()