import os

os.system("python src/load_data.py")
os.system("python src/clean_data.py")
os.system("python src/transform.py")
os.system("python src/analyze.py")
os.system("python src/report.py")

print("\nProject Executed Successfully.")