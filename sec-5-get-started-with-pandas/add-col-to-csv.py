# Creater a scipr that iterates through csv file using for loop, and reads csv file as pandas DF and add empty col as a DF and populate that col with values
# Each of the col cells with the values; These values will be the name of th files that will be iterated.

# Name of the station - 0100010-99999

# Create a new col at the end of the file that has the stationame in each of the cells 
# At the end, concat all the files into a sinlge DF 

import os
import pandas
import glob

def addField():
    os.chdir('./Extracted')
    fileList=glob.glob('*')
    for filename in fileList:
        df=pandas.read_csv(filename,sep='\s+',header=None)
        df['Station']=[filename.rsplit('-',1)[0]]*df.shape[0]            # df.shape --> Gives Number of rows
        df.to_csv(filename+'.csv',index=None,header=None)
    
addField()






