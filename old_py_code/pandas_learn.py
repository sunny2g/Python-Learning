
# Learning pandas

import pandas as pd 
import numpy as np

# We can create a list by passing on objects in pandas

series1=pd.Series([1,2,3,4,'abc'])

print(series1)

# Creating a Dataframe by passing a numpy array, with a datetime index using date_range( ) and labelled columns

dates=pd.date_range("20230106",periods=6)
dates

df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list("DEFG"))

df

#Creating a dataframe by passing a dictionary of objects that can be converted into a series like structure

df2=pd.DataFrame(
    {
        "A":1.0,
        "B":pd.Timestamp("20130102"),
        "C":pd.Series(1,index=list(range(4)),dtype="float32"),
        "D":np.array([3]*4,dtype="int32"),
        "E":pd.Categorical(["test","train","test","train"]),
        "F":"foo",
    }
)

df2

# The Columns of dataframe has different data types.

df2.dtypes

# Use Use DataFrame.head() and DataFrame.tail() to view the top and bottom rows of the frame respectively.

df.head()

df.tail()

# Display the DataFrame.index or DataFrame.columns.

df.index

df.columns

# DataFrame.to_numpy() gives a numpy presentation to underlying data.
# This can be expensive operation when dataframe has columns with many data types.
# Numpy has one dtype for entire array while pandas Dataframes have one dtype per column.
# DataFrame.to_numpy() does not include the index or column labels in the output.

df.to_numpy()

df2.to_numpy()

# Describe() shows a quick statistic summary of your data. 

# Transposing your data with df.T 

df.T 

# DataFrame.sort_index() sorts by an axis

df.sort_index(axis=1,ascending=False)

df.sort_index(axis=1,ascending=True)

# DataFrame.sort_values() sorts by values

df.sort_values(by="D")

# Selection in pandas

df["D"]

# Selecting via [] (_getitem_), which slices the rows

df[0:3]

# Selection by label, for getting a cross section using  a label

df.loc[dates[1]]

# Selecting on a Multi Axis By Label

df.loc[:, ["D", "E"]]

# For getting a scalar value

df.loc[dates[0], "D"]

df.at[dates[0], "D"]

# Select Via the position of the passed integers

df.iloc[3]

# By Selecting Integer Slices 

df.iloc[3:5,0:2]

# By The List Of Integers

df.iloc[[1,2,4],[2,3]]

# For Slicing Rows Explicitely

df.iloc[1:3,:]

# Using Single Columns value to select data

df[df["D"]>0]

# Selecting values from a dataframe where condition is met

df[df>0]

# Using the isin() method for filtering 

df2 = df.copy()

df2["C"]=["one","two","three","four","five","six"]

df2[df2["C"].isin(["two","four"])]

# Setting a new column automatically aligns the data by the indexes 

s1 = pd.Series([1,2,3,4,5,6],index=pd.date_range("20230106",periods=6))

df["B"]=s1

df

# Settings Values By Labels

df.at[dates[0], "B"] = 0

df.at[dates[1], "D"] = df.at[dates[1], "D"] * 3

df

