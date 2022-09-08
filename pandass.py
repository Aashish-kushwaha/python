'''
pandas is a python package providing fast , flexible, and expressive
data structures designed to make working with "relational" or "labeled"
data both easy and intuitive.it is well suited for many different kind
of data like tabular data , ordered and unordered time series data,
arbitrary matrix data,statiscal data sets
the two primary  data structures of pandas are
-> series(1-dimensional):1D labeled homogeneously-typed array, access label is called as index.
pandas series has no column labels as it is just a single columnof dataFrame
-> DataFrame(2-Dimensional): general 2D labeled, size-mutable tabular with potentially
heterogeneously-typed column,

pandas is bulit on top of numpy and is intended to integrate with other 3rd party
libraries.

features of pandas
1.flexible eshaping and providing of data sets
2.make it easy to convert differently-indexed data in other python and numpy data
structures
3.robust IO tools for loading data from flat files(CSV and delimited), Excel files,
datbases, and saving from ultrafast HDF5 format

uses:stock pridiction,recomdation system clean the inconsistancy of data
'''

import pandas as pd
import numpy as np

print("creating series")
s=pd.Series([1,2,3,4,5,6,7,np.nan,8,9,10])  #np.nan means not a number which is used to replace any missing numerical value
print(s)
print("max and min for series")
print(s.max())
print(s.min())
print("creating DataFrame")
d=pd.DataFrame({'A':[1,2,3,5,6,7],
                'B':['a','b','s','e','t','y'],
                'C':[10.0,13.0,24.0,56.0,21.0,90.0]})  #table has two columns A,B and three rows
print(d)

print("printing particular column of Data Frame")
print(d['A'])
print("max and min of particular column")
print(d["A"].max())
print(d['B'].min())

print("some basic statistics of the numerical data in the table")
print(d.describe()) #it gives count,mean,std,min,max etc


print("slicing")
print(d[0:2])

print("label slicing")
print(d.loc['0':'2',['A','C']])

print("exact value")
print(d.at[2,'C'])

 