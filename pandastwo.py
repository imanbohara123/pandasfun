import pandas as pd
# print(df.iloc[1]) # Selects the row at index position 1
# print(df.iloc[1:3]) # Selects rows 1 and 2 (Python slicing is end-exclusive).
# print(df.iloc[1:3,0:2]) # Selects rows 1 and 2 AND columns 0 and 1 (again, slice is end-exclusive)

df = pd.DataFrame({
    'Name': ['John', 'Kate', 'Leo', 'Mia'],
    'Department': ['IT', 'HR', 'Sales', 'Finance'],
    'Salary': [50000, 55000, 60000, 65000]})
# print(df)
# print(df.iloc[1])
# print("hello",df.iloc[1:3])
# print(df.iloc[1:3,0:2])