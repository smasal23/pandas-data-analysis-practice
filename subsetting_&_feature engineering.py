# Data Manipulation/ Sub-setting(Data Extraction, Data Filtering)
# Sub-setting - Creating a sub table out of the whole data.
# Manipulations i.e. modifications can be done column-wise, row-wise, condition-wise, both row & column - wise and datatype-wise.
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv("F:\\onedrive\\Desktop\\DATA SCIENCE\\Data Handling - Pandas\\stores.csv")

print(df.head())


# Based on Datatype
# Subset based on object vars
df2 = df.select_dtypes(include = 'object')
print(df2.head(2))

# Subset based on numeric var
df3 = df.select_dtypes(include = 'number')
print(df3.head(2))

# Subset based on float and object var
df4 = df.select_dtypes(include = ['float', 'object'])
print(df4.head(2))


# Based on Columns
print(df.columns)
df5 = df[['Location', 'OperatingCost', 'TotalSales']] # the extra square bracket is used for indexing.
print(df5.head(2))


# Based on data filter(conditions) i.e. Data Subsetting
# Numeric Condition 1
df6 = df[(df["TotalSales"] > 300)]
print(df6.head())

# Condition 2
df7 = df[df["Location"] == 'Delhi']
print(df7.head(2))

# Create a new subset of data where Location is Delhi and Total Sales are greater than 300
df8 = df[(df["TotalSales"] > 300 ) & (df["Location"] == "Delhi")]  # Remember to use and = &, | = or
print(df8.head())
# Location is Delhi, Mumbai and Chennai
df9 = df[df["Location"].isin(['Delhi', 'Mumbai', 'Chennai'])]
print(df9)  # Remember head()
# Where total sales > 100 and < 200
df10 = df[df["TotalSales"].between(100,200)]
print(df10)


#* Based on rows(observations)
#* Difference between loc and iloc
# When df is declared with square brackets, the first entry will always be rows and second will always be columns.
# loc will print data in terms of column_names
df11 = df.loc[:,['Location', 'TotalSales']]
print(df11)
# iloc will print data in terms of column position.
df12 = df.iloc[:,[3, 6]]
print(df12)
# filter first 10 rows
df13 = df.iloc[0:10, :]
print(df13)
df14 = df.iloc[0:10, 0:3]
print(df14)


# Data Cleaning/ Feature Engineering
# Create new variable - profit
df['Profit'] = df['TotalSales'] - df['OperatingCost']
print(df.head())
# Create yearly total sales
df['YearlyTotalSales'] = df['TotalSales'] * 12
print(df.head())

# Drop or delete variables
#* Difference between axis 1 & 0 and what is inplace = true
# Delete Column
df.drop('Location', axis = 1, inplace = True) # axis determines column and inplace will remove it permanently from ds.
print(df.head())
# Delete Row
df.drop(3, axis = 0, inplace = True) # axis determines row and inplace will remove it permanently from ds.
print(df.head())
# Delete Multiple Columns
df.drop(['Location', 'StoreType'], axis = 1, inplace = True)
# Delete Multiple Rows
df.drop([3, 5, 8, 20], axis = 0, inplace = True)

# Renaming Column Name
df = pd.read_csv("F:\\onedrive\\Desktop\\DATA SCIENCE\\Data Handling - Pandas\\stores.csv")
print(df.head())

df = df.rename(columns = {'Location' : 'City'})
print(df.head())