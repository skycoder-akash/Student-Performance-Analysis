import pandas as pd

df = pd.read_csv("data/student_dataset_v2.csv")

print("=" * 60)
print("      STUDENT PERFORMANCE DATA HANDLING SYSTEM")
print("=" * 60)

# Display first 5 records
print("\n1. First 5 Records")
print(df.head())

# Display last 5 records
print("\n2. Last 5 Records")
print(df.tail())

# Display shape of dataset
print("\n3. Dataset Shape")
print("Rows :", df.shape[0])
print("Columns :", df.shape[1])

# Display column names
print("\n4. Column Names")
print(df.columns.tolist())

# Display data types
print("\n5. Data Types")
print(df.dtypes)