# import pandas as pd
# #The process reading excel files
# df = pd.read_csv(r'C:\Users\Iman bohare\Desktop\sql\sql practice.csv')
# # df.to_csv('output.csv',index=False)
# print(df)
#Note : Above C:\Users\Iman bohare\Desktop\sql given due to the excel file not
# in the same folder so entered above one

#Add new one row to this excel files
# nayaone = {
#     'Name':'Ram',
#     'Department':'IT',
#     'Salary':45000
# }
# df =pd.concat([df.iloc[:1],nayaone,df.iloc[1:]]).reset_index(drop=True)
# print(df)

# #For json 
# #Reading
# df = pd.read_json('file.json')
# #writing
# df.to_json('output.json')

# #parquet:column based binary files format use to store large dataset
# #Reading
# df=pd.read_parquet('file.paequet')
# #Writing
# df.to_parquet('Output.parquet')\

#Dataexploration
# df.head() top row views
#df.tail() view bottom column
#Data types
#check for missing values
#df.isnull().sum()