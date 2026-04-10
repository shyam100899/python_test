import pandas as pd

s1=pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(s1)
print(s1.iloc[[0,2]]) #by position
print(s1.loc[['a','c']]) #by lab
