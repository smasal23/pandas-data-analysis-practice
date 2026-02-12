# pandas - panel data analysis(time series and cross-sectional data)
#        - data frame - entire sheet and series - single column within a table.
# Data Analytics - 1] import packages
#                  2] import data(connect with data)
#                  3] understanding data
#                  4] cleaning data

# Import required packages
import pandas as pd # pd - pseudonym of package
import numpy as np

print(dir(pd)) # prints all the functions present in the library.

# Import csv data file
df = pd.read_csv("F:\\onedrive\\Desktop\\DATA SCIENCE\\Data Handling - Pandas\\stores.csv")

# Import excel data file
#df_2 = pd.read_excel("F:\\onedrive\\Desktop\\DATA SCIENCE\\Data Handling - Pandas\\stores.xlsx")

# Data Understanding
#* head() - gives first 5 rows of the data
print(df.head())
print(df.head(10))

# tail() - gives last 5 rows of the data
print(df.tail())

# sample() - gives random observations of the data
print(df.sample(5))

#* info() - gives all information of your data
print(df.info())
# the non-null column specifies null values in the data
# dtype for str in pandas as objects

# shapes() - gives no. of rows and columns
print(df.shape)
print(df.shape[0])
print(df.shape[1])

# type()
print(type(df))

# columns() -
print(df.columns)

#dtypes()
print(df.dtypes)

#* Checking missing values in data
df.isnull().sum()

#* describe() - Description/detail analysis of data gives statistical functions
print(df.describe().T)  # T is transpose of row and column

# select only string variables
print(df.describe(include = 'object').T) # top = most occurrences of the object, unique =

#* count number of categories(freq)
print(df['StoreType'].value_counts())

# How many stores are from Electronic Zone?
print(df['StoreName'].value_counts())