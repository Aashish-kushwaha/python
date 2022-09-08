"""
pandas is a python package providing fast , flexible, and expressive
data structures designed to make working with "relational" or "labeled"
data both easy and intuitive.it is well suited for many kind
of data like tabular data , ordered and unordered time series data,
arbitrary matrix data,statistical data sets
the two primary  data structures of pandas are
-> series(1-dimensional):1D labeled homogeneously-typed array, access label is called as index.
pandas series has no column labels as it is just a single column of dataFrame
-> DataFrame(2-Dimensional): general 2D labeled, size-mutable tabular with potentially
heterogeneously-typed column,

pandas is built on top of numpy and is intended to integrate with other 3rd party
libraries.

features of pandas
1.flexible reshaping and providing of data sets
2.make it easy to convert differently-indexed data in other python and numpy data
structures
3.robust IO tools for loading data from flat files(CSV and delimited), Excel files,
databases, and saving from ultrafast HDF5 format

uses:stock prediction,recommendation system clean the inconsistency of data
"""

import pandas as pd
import numpy as np

print("creating series")
s = pd.Series([1, 2, 3, 4, 5, 6, 7, np.nan, 8, 9,
               10])  # np.nan means not a number which is used to replace any missing numerical value
print(s)
print("max and min for series")
print(s.max())
print(s.min())
print("creating DataFrame")
d = pd.DataFrame({'A': [1, 2, 3, 5, 6, 7],
                  'B': ['a', 'b', 's', 'e', 't', 'y'],
                  'C': [10.0, 13.0, 24.0, 56.0, 21.0, 90.0]})  # table has two columns A,B and three rows
print(d)

print("printing particular column of Data Frame")
print(d['A'])
print("max and min of particular column")
print(d["A"].max())
print(d['B'].min())

print("some basic statistics of the numerical data in the table")
print(d.describe())  # it gives count,mean,std,min,max etc

print("slicing")
print(d[0:2])

print("label slicing")
print(d.loc['0':'2', ['A', 'C']])

print("exact value")
print(d.at[2, 'C'])

print("boolean indexing")
print(d[d['A'] > 3])  # shows all the values which are greater than 3 in column A
print((d[d['B'] == 'e']))  # shows all the value in which B column has value 'e'

'''
HANDLING MISSING VALUE
missing data or null values in a data can create a lot of ruckus in other stages of data
science life cycle,it is very important to deal with the missing dta in an effective manner.
'''
# reindexing:reindexing in pandas can be used to change the index of rows and columns of dataFrame.
# one can reindex a single row or multi ple rows using reindex() method.
# default values in the new index that are not present in the dat frame are assigned NaN

column = ['a', 'b', 'c', 'd', 'e']
index = [1, 2, 3, 4, 5]

df = pd.DataFrame(np.random.rand(5, 5), columns=column, index=index)

print(df)

print("reindex data:")
print(df.reindex([2, 4, 1, 5, 3]))

'''
pandas OPERATION
->descriptive statistics operation
->applying function to the data
->string processing operations
->histogramming
'''
# descriptive operation
print(df.mean())
print()
print(df.mean(1))
print()
ss=pd.Series([1,2,3,np.nan,4,5,6,7,8,9],index=[1,2,3,4,5,6,7,8,9,10]).shift(2)
print()
print(ss)

# applying function
print(df.apply(lambda x:x.max()-x.min()))
