# Concat all the csv files in Extracted folder into a single csv file

import os
import pandas
import glob

def concat():
    os.chdir('./Extracted')
    fileList=glob.glob('*')
    dfList=[]
    colnames=["Year", "Month", "Day", "Hour", "Temp", "DewTemp", "Pressure", "WindDir", "WindSpeed", "Sky", "Precip1", "Precip6", "ID"]
    # ID is the new col you add.
    # The above list values are from a specific file in the ftp URL
    for filename in fileList:
        print(filename)
        df=pandas.read_csv(filename, header=None)
        dfList.append(df)
    concatDf=pandas.concat(dfList,axis=0)   # axis is to concat vertically
    concatDf.columns=colnames
    concatDf.to_csv=(FilePath='./Extracted', index=None)

concat()

