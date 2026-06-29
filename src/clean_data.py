import pandas as pd

# Read dataset
df = pd.read_csv("data/student_dataset_v2.csv")

print("=" * 60)
print("MODULE 3 : DATA CLEANING")
print("=" * 60)

# -------------------------------
# Remove duplicate records
# -------------------------------
duplicates = df.duplicated().sum()
print("\nDuplicate Records Found :", duplicates)

df = df.drop_duplicates()

# -------------------------------
# Handle missing values
# -------------------------------
print("\nMissing Values Before Cleaning")
print(df.isnull().sum())

# Fill numeric missing values with column mean
df["StudyHours"] = df["StudyHours"].fillna(df["StudyHours"].mean())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Fill missing names with "Unknown"
df["Name"] = df["Name"].fillna("Unknown")

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

# -------------------------------
# Remove invalid entries
# -------------------------------

# Attendance should be between 0 and 100
df = df[(df["Attendance"] >= 0) & (df["Attendance"] <= 100)]

# Study Hours should be >= 0
df = df[df["StudyHours"] >= 0]

# Marks should be between 0 and 100
df = df[(df["Marks"] >= 0) & (df["Marks"] <= 100)]

print("\nData cleaned successfully.")

# -------------------------------
# Save cleaned dataset
# -------------------------------
df.to_csv("output/cleaned_data.csv", index=False)

print("\nCleaned dataset saved as:")
print("output/cleaned_data.csv")