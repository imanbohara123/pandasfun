import pandas as pd

#Series: hold one-dimentional labeled array one column data
# series = pd.Series([1,2,3,4,5,6])
# print(series)
#datafreame: hold two-dimentional or multiple column of data heres

# dataframe = pd.DataFrame({'A':[1,2],'B':[3,4]})
# print(dataframe)


# Write a Python program using Pandas to create a table that contains the following columns and data:

# Employee Name: John, Kate, Leo

# Department: IT, HR, Sales

# Salary: 50000, 55000, 60000



# Answer: #Using dictonary
# employeedata = pd.DataFrame({'Employee Name':['john','kate','leo'],'Department': ['IT','HR','Sales'],'Salary':[50000,55000,60000]})
# print(employeedata)

# #above samedata represent using lists
# #Using lists
# #Answer:
# rawdata = ['john','kate','leo'],['IT','HR','Sales',],[50000,55000,60000]
# employeedata = pd.DataFrame(rawdata,columns=['Employee Name','Department','Salary'])
# print(employeedata)