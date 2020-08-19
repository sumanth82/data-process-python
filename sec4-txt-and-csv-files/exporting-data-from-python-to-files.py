# Export df1 frame to a column separated file

import pandas

df1 = pandas.read_csv('./comma-separated.txt')
print(df1.head)

# O/P; Year  Month  Day  Hour  Temp  DewTemp  Pressure  WindDir  WindSpeed  Sky  Precip1  Precip6
#0    1912      4    1     6   114       94     10121      200        120    8    -9999    -9999
#1    1912      4    1     9   146       96     10122      240        140    8    -9999    -9999
#2    1912      4    2     6   172      122     10146      210         40    2    -9999       40
#3    1912      4    2     9   193    -9999     10150      240        210    1    -9999        0
#4    1912      4    2    12   188      125     10152      240        250    1    -9999        0

#Now to export this df1 frame/data to a csv:

df1.to_csv('ColnSeparatedexport.txt', sep=':')
df1.to_csv('comma-separated.csv')

# NOTE : Use pandas.DataFrame.to_csv? to get the details on the method from the REPL 

# For no header and a separate index_col 

#df1.to_csv('comma-separated.csv', header=None, index_col=2)







