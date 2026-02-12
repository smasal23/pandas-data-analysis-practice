import pandas as pd
import numpy as np
#* Merging and Joining
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40]
})

print(df1)

df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'City': ['London', 'Paris', 'New York', 'Tokyo'],
    'Occupation': ['Engineer', 'Artist', 'Doctor', 'Developer']
})

print(df2)

#Inner Join - This is the default join. No need to mention how.
df_inner = pd.merge(df1, df2, on = 'ID', how = 'inner')
print(df_inner.head())
# Full Join - the keyword for how is outer.
df_full = pd.merge(df1, df2, on = 'ID', how = 'outer')
print(df_full.head())
# Left Join
df_left = pd.merge(df1, df2, on = 'ID', how = 'left')
print(df_left.head())
# Right Join
df_right = pd.merge(df1, df2, on = 'ID', how = 'right')
print(df_right.head())
#
df2 = pd.DataFrame({
    'Cust_ID': [3, 4, 5, 6],
    'City': ['London', 'Paris', 'New York', 'Tokyo'],
    'Occupation': ['Engineer', 'Artist', 'Doctor', 'Developer']
})
print(df2)
#
df_left = pd.merge(df1, df2, left_on = 'ID', right_on = 'Cust_ID', how = 'left')
print(df_left.head())

#* Join() - Always join tables based on key variables, so need to use set_index(). Default join is left join.
df1.join(df2)
# Difference between Merge & Join
# Join will be able to combine multiple tables at once. Merge is faster compared to Join.


# Append
# Create two new DataFrames for appending
df_A = pd.DataFrame({
    'Product': ['Apple', 'Banana', 'Orange'],
    'Price': [1.0, 0.5, 0.75]
})

df_B = pd.DataFrame({
    'Product': ['Grape', 'Kiwi'],
    'Price': [2.5, 1.2]
})

print(df_A)
print(df_B)
# Append - axis will operate with rows and columns.
final_df = pd.concat([df_A, df_B], axis = 0)
print(final_df)
# Difference between Merge and Append - Merge will happen with key variables and Append with rows and columns.


