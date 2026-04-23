import pandas as pd

s = pd.series[1,2,3,4]
print(s)


#dtype used for type of data.
# print(df.dtypes)

# You can convert types using .astype():
# df['Age']  = df['Age'].astype('float')
# df['Name'] = df['Name'].astype('string')
# print(df.dtypes)
# print(df)


# .loc[] is used to select data by label (i.e., the index or column names).
# It is inclusive of both the start and stop when slicing.


# print(df.loc['a'])  # Select row with label 'a'
# print(df.loc['a', 'Age'])
# print(df.loc['a':'c'])
# exit()

# .iloc[] is used to select data by integer position (i.e., by row/column number, starting from 0).
# It is exclusive when slicing (the end index is not included).

# print(df.iloc[0])
# print(df.iloc[0, 0])   #for a single column value 
# print(df.iloc[2, 1])   #for a single column value 
# print(df.iloc[0:2])    #give records of 0 and 1 position set



# dtype	        Meaning	        Example
# int64	        Integer         numbers	1, 2, 3
# float64	    Decimal         numbers	1.5, 3.14
# object	    Strings         or mixed types	"hello"
# bool	        Boolean values	True/False
# datetime64	Date and time	2025-01-01
# category	    Categorical	    "A", "B", "C"


# Mix Case	                Result dtype            Reason
# int + int	                int	                    Same type
# int + float	                Float	                Decimal needed
# float + int	                float	                Safe conversion
# bool + int	                int	                    True=1, False=0
# bool + float	            float	                1.0, 0.0
# int + string	            object	                Mixed types
# float + string	            object	                Mixed types
# bool + string	            object	                String dominates
# string + string	            object/string	        Pure text
# string numbers ('1','2')	object	                Still text
# mixed (all types)	        object	                Safest fallback
