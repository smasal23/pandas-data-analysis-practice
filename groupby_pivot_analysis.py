# New Data Importing
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv("F:\\onedrive\\Desktop\\DATA SCIENCE\\Data Handling - Pandas\\online_gaming_behavior_dataset.csv")
print(df.head())
print(df.info())

print(df.columns)
print(df.describe().T)
# for categorical data
print(df.describe(include = 'object').T)

# Data Analysis
# group by - Happens only on the categorical variables
print(df[['Gender', 'Age']].groupby('Gender').mean())

print(df[['Gender', 'Location', 'PlayTimeHours']].groupby(['Gender', 'Location']).mean())
# What is minimum playtime hours by engagementlevel?
print(df[['EngagementLevel', 'PlayTimeHours']].groupby('EngagementLevel').min())
# requires matplotlib.pyplot
#print(df[['EngagementLevel', 'PlayTimeHours']].groupby('EngagementLevel').min().plot(kind='bar'))
# Multiple stats
df_summary = df[['Gender', 'Age']].groupby('Gender').agg(['mean', 'std', 'min', 'max']).round(2)

# Export Data - %pwd - print working directory
df_summary.to_excel("F:\\onedrive\\Desktop\\DATA SCIENCE\\Data Handling - Pandas\\df_summary.xlsx")

# Pivot - similar to groupby, but an efficient way of structurizing data
print(pd.pivot_table(df,
               index = 'Location',
               columns = 'Gender',
               values = 'Age',
               aggfunc = 'mean').round(2))

print(pd.pivot_table(df,
               index = ['Location', 'EngagementLevel'],
               columns = ['Gender', 'GameGenre'],
               values = 'Age',
               aggfunc = 'mean').round(2))

# How many male and female are from different location?
print(df[['Location', 'Gender', 'PlayerID']].groupby(['Location', 'Gender']).count())
# What is the average session per week by game genre?
print(df[['SessionsPerWeek', 'GameGenre']].groupby('GameGenre').mean())
# What is total playing hours from young gamers? # Can't groupby for numerical values
df['young_person'] = pd.cut(df['Age'], 2, labels = ['Young', 'Old'])
# print(df['young_person'])
print(df[['PlayTimeHours', 'young_person']].groupby('young_person', observed = True).sum())

