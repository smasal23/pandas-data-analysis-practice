# Data Manipulation(contd.)
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv("F:\\onedrive\\Desktop\\DATA SCIENCE\\Data Handling - Pandas\\stores.csv")
print(df.head())

#* Sorting values
#* ascending = True will ascend the fields and ascending = False will descend the fields.
# ascending
df.sort_values(by = ("TotalSales"), ascending = False, inplace = True)
print(df.head())
#* descending
df.sort_values(by = ("TotalSales"), ascending = True, inplace = True)
print(df.head())
#* we cannot sort two numerical fields together.
#* we can sort categorical values with numerical values together.
df.sort_values(by = ["Location", "TotalSales"], ascending = True, inplace = True)
print(df.head())
#* A Category in ascending and Numerical in descending.
df.sort_values(by = ["Location", "TotalSales"], ascending = [True, False], inplace = True)
print(df.head())


# Feature Transformation - Binning
# This converts numerical data into categorical data.
# Infer
df['Store_performance'] = pd.cut(df['TotalSales'], 3, labels = ['High', 'Medium', 'Low'])
#df['Store_performance'] = pd.cut(df['TotalSales'], [0,100,300,1000], labels = ['High', 'Medium', 'Low'])
df['Store_performance'].value_counts()
print(df.head(20))


# Data Type Conversion
# num to str
# str to num
# str to date
#df['TotalSales'] = df['TotalSales'].apply(pd.to_numeric)
#print(df.head(20))

df['TotalSales'] = df['TotalSales'].astype('int64')
print(df.head())


# Index(search faster)
df.set_index('StoreCode', inplace = True)
print(df.head())
# reset_index
df.reset_index(inplace = True)
print(df.head())


# Data Cleaning
# Duplicates - Check using a unique variable
print(sum(df['StoreCode'].duplicated()))
# After checking drop duplicates
df['StoreCode'].drop_duplicates()

# Missing Values
# Checking Missing Values
print(df.isnull().sum())
# Either drop missing or impute(recommended) - fill missing values with mean(numeric) and mode(object) and median(outliers) of that field
# Drop Missing
#df = df['AcqCostPercust'].dropna()
# Impute Missing
print(df['AcqCostPercust'].mean())
df['AcqCostPercust'] = df['AcqCostPercust'].fillna(3.65)
print(df.isnull().sum())

# Combine Two Variables
df['StoreAddress'] = df['StoreCode'] + '-' + df['StoreName']
print(df.head())
# Split an object
df[['code', 'name']] = df['StoreAddress'].str.split('-', expand = True)
print(df.head())


# What is average of TotalSales?
print(df['TotalSales'].mean())

# How many stores have low operating cost?
df['Store_performance'] = pd.cut(df['OperatingCost'], 3, labels = ['Low', 'Medium', 'High'])
print(df.head(20))
print((df['Store_performance'] == 'Low').sum())