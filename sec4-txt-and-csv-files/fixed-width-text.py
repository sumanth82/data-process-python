# Reading fixed width text files

# If you see the text file - fixed-width.txt, it has column headers with different spacing. For this uneven files types use read_fwf() - method. 
#read_fwf() - fixedwidthfile

import pandas

df1=pandas.read_fwf('fixed-width.txt')
print(df1.head())



