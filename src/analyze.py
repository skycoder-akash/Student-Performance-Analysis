import pandas as pd

# Read transformed dataset
df = pd.read_csv("output/cleaned_data.csv")

print("=" * 60)
print("MODULE 5-9 : ANALYSIS")
print("=" * 60)

# ==========================================================
# MODULE 5 : DATA FILTERING
# ==========================================================

print("\nMODULE 5 : DATA FILTERING")

# Top Performing Students (Marks >= 90)
toppers = df[df["Marks"] >= 90]
toppers.to_csv("output/toppers.csv", index=False)

# Failed Students
failed_students = df[df["Result"] == "Fail"]
failed_students.to_csv("output/failed_students.csv", index=False)

# Attendance below 75%
low_attendance = df[df["Attendance"] < 75]
low_attendance.to_csv("output/low_attendance.csv", index=False)

# Study Hours greater than 8
high_study_hours = df[df["StudyHours"] > 8]
high_study_hours.to_csv("output/high_study_hours.csv", index=False)

print("Filtering Completed Successfully.")

# ==========================================================
# MODULE 6 : DATA ANALYSIS
# ==========================================================

print("\nMODULE 6 : DATA ANALYSIS")

print("\nAverage Marks :", df["Marks"].mean())

print("Highest Marks :", df["Marks"].max())

print("Lowest Marks :", df["Marks"].min())

print("Average Attendance :", df["Attendance"].mean())

print("Average Study Hours :", df["StudyHours"].mean())

pass_percentage = (df["Result"] == "Pass").mean() * 100
fail_percentage = (df["Result"] == "Fail").mean() * 100

print("Pass Percentage :", round(pass_percentage,2), "%")
print("Fail Percentage :", round(fail_percentage,2), "%")

print("\nGrade Distribution")
print(df["Grade"].value_counts())

# ==========================================================
# MODULE 7 : SORTING
# ==========================================================

print("\nMODULE 7 : SORTING")

print("\nStudents Sorted by Marks")
print(df.sort_values(by="Marks", ascending=False))

print("\nStudents Sorted by Attendance")
print(df.sort_values(by="Attendance", ascending=False))

print("\nStudents Sorted by Study Hours")
print(df.sort_values(by="StudyHours", ascending=False))

# ==========================================================
# MODULE 8 : GROUPING
# ==========================================================

print("\nMODULE 8 : GROUPING")

print("\nAverage Marks by Grade")
print(df.groupby("Grade")["Marks"].mean())

print("\nStudents in Each Grade")
print(df.groupby("Grade").size())

print("\nAverage Attendance by Grade")
print(df.groupby("Grade")["Attendance"].mean())

# ==========================================================
# MODULE 9 : STATISTICAL ANALYSIS
# ==========================================================

print("\nMODULE 9 : STATISTICAL ANALYSIS")

print("\nMean")
print(df[["Marks","Attendance","StudyHours"]].mean())

print("\nMedian")
print(df[["Marks","Attendance","StudyHours"]].median())

print("\nMode")
print(df[["Marks","Attendance","StudyHours"]].mode())

print("\nStandard Deviation")
print(df[["Marks","Attendance","StudyHours"]].std())

print("\nVariance")
print(df[["Marks","Attendance","StudyHours"]].var())

print("\nCorrelation Matrix")
print(df[["Marks","Attendance","StudyHours","PerformanceScore"]].corr())

print("\nModules 5-9 Completed Successfully.")