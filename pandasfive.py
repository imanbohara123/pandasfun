import pandas as pd

data = {
    "Name": ["John", "Kate", "Leo"],
    "Age": [25, 28, 30],
    "Department": ["IT", "HR", "Sales"],
    "Salary": [50000, 55000, 60000]
}

data = pd.DataFrame(data)
print(data)
