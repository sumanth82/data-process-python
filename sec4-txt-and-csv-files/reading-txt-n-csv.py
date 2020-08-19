import pandas

df1 = pandas.read_csv('./comma-separated.txt')
print(df1.head)

# Takes Default Row as the Header:

#Year  Month  Day  Hour  Temp  DewTemp  Pressure  WindDir  WindSpeed  Sky  Precip1  Precip6
#0    1912      4    1     6   114       94     10121      200        120    8    -9999    -9999
#1    1912      4    1     9   146       96     10122      240        140    8    -9999    -9999
#2    1912      4    2     6   172      122     10146      210         40    2    -9999       40
#3    1912      4    2     9   193    -9999     10150      240        210    1    -9999        0
#4    1912      4    2    12   188      125     10152      240        250    1    -9999        0

df2 = pandas.read_csv('./comma-separated.txt', header=None)
print(df2.head)

# If you do not want to use the default header, use the above. Plus Python generates a default column called INDEX COLUMN 

#0      1    2     3     4        5         6        7          8    9        10       11
#0    Year  Month  Day  Hour  Temp  DewTemp  Pressure  WindDir  WindSpeed  Sky  Precip1  Precip6
#1    1912      4    1     6   114       94     10121      200        120    8    -9999    -9999
#2    1912      4    1     9   146       96     10122      240        140    8    -9999    -9999
#3    1912      4    2     6   172      122     10146      210         40    2    -9999       40
#4    1912      4    2     9   193    -9999     10150      240        210    1    -9999        0

# To set a specific col as an index column, do the following:

df3 = pandas.read_csv('./comma-separated.txt', index_col=3)
print(df3.head)

# The above command will set the index col to HOUR as below:

#       Year  Month  Day  Temp  DewTemp  Pressure  WindDir  WindSpeed  Sky  Precip1  Precip6
#Hour                                                                                      
#6     1912      4    1   114       94     10121      200        120    8    -9999    -9999
#9     1912      4    1   146       96     10122      240        140    8    -9999    -9999
#6     1912      4    2   172      122     10146      210         40    2    -9999       40
#9     1912      4    2   193    -9999     10150      240        210    1    -9999        0


# NOTE: re for one or more space is '\s+'

df4=pandas.read_csv('space-separated.txt', sep='\s+')

# Print the dataframe using the head method

print(df4.head())

# O/P: 

  #Year  Month  Day  Hour  Temp  DewTemp  Pressure  WindDir  WindSpeed  Sky  Precip1  Precip6
#0  1912      4    1     6   114       94     10121      200        120    8    -9999    -9999
#1  1912      4    1     9   146       96     10122      240        140    8    -9999    -9999
#2  1912      4    2     6   172      122     10146      210         40    2    -9999       40

##### NOTE - Reading an excel file

#If you come across Excel files, you'll need to use the read_excel method to open them in Python. 
#For example, if you have an Excel file with three sheets and you want to read the data contained in the first sheet, you would do this:
#df=pandas.read_excel("filename.xlsx", sheetname=0)
#For the second sheet you would pass 1 to the sheetname parameter, 2 for the third sheet and so on.


