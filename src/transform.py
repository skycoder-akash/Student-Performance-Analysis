import pandas as pd

# Read cleaned dataset
df = pd.read_csv("output/cleaned_data.csv")

print("=" * 60)
print("MODULE 4 : DATA TRANSFORMATION")
print("=" * 60)

# -------------------------------
# Grade Assignment
# -------------------------------

grade = []

for marks in df["Marks"]:
    if marks >= 90:
        grade.append("A")
    elif marks >= 80:
        grade.append("B")
    elif marks >= 70:
        grade.append("C")
    elif marks >= 60:
        grade.append("D")
    else:
        grade.append("F")

df["Grade"] = grade

# -------------------------------
# Result (Pass / Fail)
# -------------------------------

result = []

for marks in df["Marks"]:
    if marks >= 40:
        result.append("Pass")
    else:
        result.append("Fail")

df["Result"] = result

# -------------------------------
# Performance Score
# Formula:
# Marks × 0.6 + Attendance × 0.2 + StudyHours × 0.2
# -------------------------------

df["PerformanceScore"] = (
    df["Marks"] * 0.6 +
    df["Attendance"] * 0.2 +
    df["StudyHours"] * 0.2
)

# -------------------------------
# Display transformed data
# -------------------------------

print("\nTransformed Dataset")
print(df.head())

# -------------------------------
# Save transformed dataset
# -------------------------------

df.to_csv("output/cleaned_data.csv", index=False)

print("\nTransformation completed successfully.")
print("Updated file saved to output/cleaned_data.csv")