import pandas as pd

#  Q1 Creating a dataset 
data = {
    "Tid": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Refund": ["Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "No"],
    "Marital Status": [
        "Single", "Married", "Single", "Married", "Divorced",
        "Married", "Divorced", "Single", "Married", "Single"
    ],
    "Taxable Income": [
        "125K", "100K", "70K", "120K", "95K",
        "60K", "220K", "85K", "75K", "90K"
    ],
    "Cheat": ["No", "No", "No", "No", "Yes", "No", "No", "Yes", "No", "Yes"]
}

df = pd.DataFrame(data)

print(df)

# Q2 Locate rows
print(df.iloc[[0, 4, 7, 8]])

# Q3 Selecting rows and columns 

print(df.iloc[3:7])

print(df.iloc[4:9,2:5])

print(df.iloc[:,1:4])

# Q4 Display rows of CSV File

from google.colab import files

uploaded = files.upload()

df = pd.read_csv("Iris.csv")
print(df.head())

# Q5 Delete row and column

df = df.drop(4)

df = df.drop(df.columns[3], axis=1)

print(df)

# Q6 Dataset about Employees

data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 38],
    "Salary": [50000, 70000, 65000, 55000, 60000],
    "Years_of_Experience": [4, 8, 10, 3, 12],
    "Joining_Date": ["2020-03-15", "2017-07-19", "2013-06-01", "2021-02-10", "2010-11-25"],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Bonus": [5000, 7000, 6000, 4500, 5000],
    "Rating": [4.5, 4.0, 3.8, 4.7, 3.5]
}

df = pd.DataFrame(data)
df.to_csv("employees.csv", index=False)
print(df)

print(df.shape)

print(df.info())

print(df.describe())

print("First 5 rows:")
print(df.head(5))
print("\nLast 3 rows:")
print(df.tail(3))

print("Average Salary:", df["Salary"].mean())
print("Total Bonus:", df["Bonus"].sum())
print("Youngest Age:", df["Age"].min())
print("Highest Rating:", df["Rating"].max())

df = df.sort_values(by="Salary", ascending=False)
print("\nDataFrame sorted by Salary:")
print(df)

def performance_category(rating):
    if rating >= 4.5:
        return "Excellent"
    elif rating >= 4.0:
        return "Good"
    else:
        return "Average"
df["Performance"] = df["Rating"].apply(performance_category)
print("\nPerformance Category:")
print(df[["Name", "Rating", "Performance"]])

print("\nMissing Values:")
print(df.isnull().sum())

df = df.rename(columns={"Employee_ID": "ID"})
print("\nAfter renaming:")
print(df)

print("\nEmployees with more than 5 years of experience:")
print(df[df["Years_of_Experience"] > 5])
print("\nEmployees in IT department:")
print(df[df["Department"] == "IT"])

df["Tax"] = df["Salary"] * 0.10
print("\nDataFrame with Tax:")
print(df)

df.to_csv("modified_employees.csv", index=False)
print("\nModified dataset saved as modified_employees.csv")
