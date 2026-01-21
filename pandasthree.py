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

#Removing the columns
#df = df.drop(columns=["columnsn"])
#df=df.drop([5]) use for the drop row of data table

#set the name column as index 
#df.set_index('names',inplace = True)
#The loc use for the indexing the categories data and iloc use for category as well as numeric
#Can plot through the pandas but not useful through pandas
#loc is use for the slicing and indexing


#df = df.dropna(axis=1) column will minus not row will constant
#df_clean = pd.Dataframe(df_nan['age']).fillna(df_nan[age].median()))
#The null values filled by the fillna(30any value enter)
#df_concat = pd.merge(df_clean,df.nam['score'].fillna(df_nan['score'].mean()),how='outer', on = df_nan['Name'])
# The how = 'any' always if one nan enter then it can't drop full row one
# #The how = 'all' can drop full row one