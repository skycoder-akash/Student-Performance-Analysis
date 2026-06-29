import pandas as pd

df = pd.read_csv("data/student_dataset_v2.csv")

print("=" * 60)
print("      STUDENT PERFORMANCE DATA HANDLING SYSTEM")
print("=" * 60)


print("\n1. First 5 Records")
print(df.head())


print("\n2. Last 5 Records")
print(df.tail())

print("\n3. Dataset Shape")
print("Rows :", df.shape[0])
print("Columns :", df.shape[1])


print("\n4. Column Names")
print(df.columns.tolist())

print("\n5. Data Types")
print(df.dtypes)

print("\n" + "=" * 60)
print("MODULE 2 : DATA INSPECTION")
print("=" * 60)


print("\n1. Missing Values")
print(df.isnull().sum())

print("\n2. Duplicate Records")
print("Duplicate Rows :", df.duplicated().sum())

# Descriptive Statistics
print("\n3. Descriptive Statistics")
print(df.describe())

# Memory Usage
print("\n4. Memory Usage")
print(df.memory_usage())

print("\nTotal Memory Used:")
print(df.memory_usage(deep=True).sum(), "bytes")

# Summary Information
print("\n5. Dataset Information")
df.info()