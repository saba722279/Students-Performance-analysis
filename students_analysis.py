import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data Acquisition
print("--- Data Acquisition ---")
try:
    data = pd.read_csv("students_performance.csv")
    print("Data loaded successfully.")
except FileNotFoundError:
    print("Error: 'students_performance.csv' not found. Please ensure the file is in the same directory.")
    exit()

print("\nFirst 5 rows:")
print(data.head())

# 2. Data Cleaning
print("\n--- Data Cleaning ---")
# Checking for missing values
missing_values = data.isnull().sum()
print("Missing Values per column:")
print(missing_values)

# Checking for duplicates
duplicates = data.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

# (Optional) Drop duplicates if any existing
if duplicates > 0:
    data = data.drop_duplicates()
    print("Duplicates removed.")

# 3. Data Analysis
print("\n--- Data Analysis ---")
# General Statistics
print("Statistics:")
print(data.describe())

# Average Scores
average_scores = data[['Math_Score', 'English_Score', 'Science_Score']].mean()
print("\nOverall Average Scores:")
print(average_scores)

# Comparison Analysis: Gender-wise performance
print("\nGender-wise Average Scores:")
gender_group = data.groupby('Gender')[['Math_Score', 'English_Score', 'Science_Score']].mean()
print(gender_group)

# 4. Visualization
print("\n--- Visualization ---")

# Set style
sns.set(style="whitegrid")

# Figure 1: Overall Average Scores
plt.figure(figsize=(8, 5))
average_scores.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])
plt.title("Overall Average Scores of Students")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.ylim(0, 100)
plt.xticks(rotation=0)
plt.savefig("average_scores.png") # Save the plot
print("Saved 'average_scores.png'")
# plt.show() # Commented out to avoid blocking execution

# Figure 2: Gender Comparison (Grouped Bar Chart)
try:
    gender_group.plot(kind='bar', figsize=(10, 6))
    plt.title("Comparison of Average Scores by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Average Scores")
    plt.ylim(0, 100)
    plt.legend(title="Subjects")
    plt.xticks(rotation=0)
    plt.savefig("gender_comparison.png") # Save the plot
    print("Saved 'gender_comparison.png'")
    # plt.show() # Commented out to avoid blocking execution
except Exception as e:
    print(f"Could not create comparison plot: {e}")

print("\nAnalysis Complete.")
