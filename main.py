import pandas as pd
import matplotlib.pyplot as plt

# read the data file
project_raw_df = pd.read_csv('./Project_File.csv')

# region
europe_df = project_raw_df.filter(items =['year_month', ' United Kingdom ', ' Germany ', ' France ', ' Italy ', ' Netherlands ',
       ' Greece ', ' Belgium & Luxembourg ', ' Switzerland ', ' Austria ',
       ' Scandinavia ', ' CIS & Eastern Europe '])

# print first 5 rows
print(europe_df.head())

# print all column name
print(europe_df.columns)

# split the "year_month" to keep the year only
europe_df["year"] = europe_df["year_month"].str.split().str[0]

# print first 5 rows
print(europe_df.head())

# change "year" column to integer
europe_df["year"] = europe_df["year"].astype("int")
print(europe_df.dtypes)

# use loc to filter 2008 - 2017
project_10year_df = europe_df.loc[(europe_df["year"] >= 2008) & (europe_df["year"] <= 2017)]

# verify the filtering
print(project_10year_df.head())
print(project_10year_df.tail())

# sum
project_sum_df = project_10year_df.groupby(by="year").sum()

# print sum to verify
print(project_sum_df)

# bar chart
# project_raw_df = project_sum_df.plot(kind='bar', x='country', y='visitors')

# print bar chart
# print(project_raw_df)

# Initialize the lists for X and Y
data = project_sum_df

df = pd.DataFrame(data)

X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])

# Plot the data using bar() method
plt.bar(X, Y, color='g')
plt.title("Total Number of Visitors in Europe")
plt.xlabel("Countries")
plt.ylabel("Number of Visitors")

# Show the plot
plt.show()