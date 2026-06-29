# Student Performance Data Handling and Analysis System using Pandas

## Project Overview

This project is developed using Python and the Pandas library to perform complete data handling and analysis on student performance data. It demonstrates the complete data lifecycle, including loading, cleaning, transforming, analyzing, and exporting data from a CSV dataset.

## Technologies Used

* Python
* Pandas
* Matplotlib (Optional Bonus)
* CSV Files
* Git & GitHub

## Project Structure

```
Student_Data_Project/
│
├── data/
│   └── student_dataset_v2.csv
│
├── output/
│   ├── cleaned_data.csv
│   ├── toppers.csv
│   ├── failed_students.csv
│   ├── low_attendance.csv
│   ├── high_study_hours.csv
│   └── report.csv
│
├── src/
│   ├── load_data.py
│   ├── clean_data.py
│   ├── transform.py
│   ├── analyze.py
│   └── report.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Features

### Module 1: Data Loading

* Read CSV file
* Display first and last five records
* Display dataset shape
* Display column names
* Display data types

### Module 2: Data Inspection

* Check missing values
* Check duplicate records
* Display descriptive statistics
* Display memory usage
* Display dataset information

### Module 3: Data Cleaning

* Remove duplicate records
* Handle missing values
* Validate study hours
* Validate attendance
* Validate marks
* Export cleaned dataset

### Module 4: Data Transformation

* Assign grades
* Generate pass/fail result
* Calculate performance score

### Module 5: Data Filtering

* Top-performing students
* Failed students
* Low attendance students
* High study hour students

### Module 6: Data Analysis

* Average marks
* Highest and lowest marks
* Average attendance
* Average study hours
* Pass percentage
* Fail percentage
* Grade distribution

### Module 7: Sorting

* Sort by marks
* Sort by attendance
* Sort by study hours

### Module 8: Grouping

* Average marks by grade
* Student count by grade
* Average attendance by grade

### Module 9: Statistical Analysis

* Mean
* Median
* Mode
* Standard deviation
* Variance
* Correlation matrix

### Module 10: Report Generation

* Generate final report
* Export report.csv

### Module 11: Export Data

Generated output files:

* cleaned_data.csv
* toppers.csv
* failed_students.csv
* low_attendance.csv
* high_study_hours.csv
* report.csv

## How to Run

1. Install the required libraries

```
pip install -r requirements.txt
```

2. Run the project

```
python main.py
```

## Author

**Akash Verma**

B.Tech Computer Science Engineering
