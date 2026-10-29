import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employee.csv")

print("Employee Details")
print(df[["Name", "Department", "Salary"]].to_string(index=False))

avg_salary = df.groupby("Department")["Salary"].mean()

print("\nAverage Salary by Department")
print(avg_salary.round(2))