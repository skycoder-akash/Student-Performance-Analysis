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