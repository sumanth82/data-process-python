# DataFrame is what holds the data in Pandas
# 

import pandas, os

df1=pandas.read_csv('SmallFile.csv', index_col=0)
print(df1.head())

# O/P:        Year  Month  Day  Hour  Temp  DewTemp  Pressure  WindDir  WindSpeed
#ID                                                                        
#Day 1  1912      4    1     6   114       94     10121      200        120
#Day 2  1912      4    1     9   146       96     10122      240        140
#Day 3  1912      4    2     6   172      122     10146      210         40
#Day 4  1912      4    2     9   193    -9999     10150      240        210
#Day 5  1912      4    2    12   188      125     10152      240        250

# In the above table, each of the entries/cells of the first row (Pressure, WindDir, WindSpeed) is identified as an IDENTIFIER of it's corresponding columns
# Identifiers are usually called column names 
# are called headers

# To fetch the values in a given identifier or a coulmn use: 
# 

df1["WindSpeed"]
print(df1["WindSpeed"])

# O/P: ID
#Day 1    120
#Day 2    140
#Day 3     40
#Day 4    210
#Day 5    250

#Name: WindSpeed, dtype: int64


# To get the AVERAGE/MEAN value of this column, use this:

print(df1["WindSpeed"].mean())

# O/P: 152.0

# To EXTRACT a ROW, use df1.loc["<Row_Name>", "<Col_Name>"] method

print(df1.loc["Day 1"])


# O/P: Year          1912
#Month            4
#Day              1
#Hour             6
#Temp           114
#DewTemp         94
#Pressure     10121
#WindDir        200
#WindSpeed      120
#Name: Day 1, dtype: int64

# To EXTRACT a PORTION of a DATAFRAME: df.loc["<Range-of-row>: <Range-of-row> ", "<Range-of-column>: <Range-of-column>"]

print(df1.loc["Day 2": "Day 4", "Temp": "Pressure"])

# O/P:        Temp  DewTemp  Pressure
#ID                            
#Day 2   146       96     10122
#Day 3   172      122     10146
#Day 4   193    -9999     10150

# To EXTRACT a VALUE of a SINGLE CELL of a PARTICULAR ROW/COL: df.loc["<index_name>", "<col_name>"]

print(df1.loc["Day 3", "Temp"])

# O/p: 172


# To ACCESS DATA using POSITIONS use df.iloc[<row_number>, <col_number>] method()

print(df1.iloc[2,4])

# O/P: 172

# To manipulate the data, pass the df value to a variable and play around 