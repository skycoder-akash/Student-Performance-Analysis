import pandas as pd

# Read transformed dataset
df = pd.read_csv("output/cleaned_data.csv")

print("=" * 60)
print("MODULE 10 & 11 : REPORT GENERATION")
print("=" * 60)

# ----------------------------
# Module 10 : Report Generation
# ----------------------------

total_students = len(df)
passed_students = len(df[df["Result"] == "Pass"])
failed_students = len(df[df["Result"] == "Fail"])

highest_marks = df["Marks"].max()
lowest_marks = df["Marks"].min()
average_marks = round(df["Marks"].mean(), 2)
average_attendance = round(df["Attendance"].mean(), 2)

grade_distribution = df["Grade"].value_counts()

print("\nTotal Students :", total_students)
print("Passed Students :", passed_students)
print("Failed Students :", failed_students)
print("Highest Marks :", highest_marks)
print("Lowest Marks :", lowest_marks)
print("Average Marks :", average_marks)
print("Average Attendance :", average_attendance)

print("\nGrade Distribution")
print(grade_distribution)

# Create Report DataFrame
report = pd.DataFrame({
    "Total Students": [total_students],
    "Passed Students": [passed_students],
    "Failed Students": [failed_students],
    "Highest Marks": [highest_marks],
    "Lowest Marks": [lowest_marks],
    "Average Marks": [average_marks],
    "Average Attendance": [average_attendance]
})

# Save report
report.to_csv("output/report.csv", index=False)

print("\nReport Generated Successfully.")
print("Saved as output/report.csv")

# ----------------------------
# Module 11 : Export Data
# ----------------------------

print("\nExported Files")

print("cleaned_data.csv")
print("toppers.csv")
print("failed_students.csv")
print("low_attendance.csv")
print("high_study_hours.csv")
print("report.csv")