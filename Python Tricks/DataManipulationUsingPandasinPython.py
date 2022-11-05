# How to import Module in Pycharm Environment
# https://blog.finxter.com/how-to-install-pandas-on-pycharm/#:~:text=Solution%20that%20always%20works%3A%201%20Open%20File%20%3E,installation%20to%20terminate%20and%20close%20all%20popup%20windows.
import pandas as pd
import numpy as np

print(np.__version__)  # Print the version
print(pd.__version__)
"""
# Declare a Dictionary

dict = {"one": [1, 2, 3, 4, 5]}
print(type(dict))

# Inbuilt Function of Pandas to create a series
my_series = pd.Series(dict)
print(type(my_series), "----", my_series)

# created a list of random numbers using randint function
a1 = np.random.randint(1, 5, size=10)
print(a1)

# Converted a1 list to Series of Pandas
series1 = pd.Series(a1)
print(series1)

# How to create DataFrame in Pandas
dict = {"id": [1, 2, 3, 4, 5], "name": ["Anand", "Kavia", "Ravi", "Shaam", "Ram"]}
#print(dict)
df = pd.DataFrame(dict)
#print(df)
#print(df.columns)
#print(df.dtypes)
"""
# Reading Files using Pandas
df = pd.read_excel("students.xlsx")
# print(df)

# Copy data into another File
# df.to_excel("mynewexportedfile.xlsx")

# Data Selection
print(df.name)
list_of_columns = ["id", "name", "compre"]
extracted = df[list_of_columns]
# print(extracted)
# print(df.loc[0])
#print(df[df.q1 > 3])

# Data Manipulation using Query
print(df.query("q1 > 3"))