# Download a range of files 

# Format of the folders and tar files in /Data folder: Ex: ftp://ftp.pyclass.com/Data/1909/028060-99999-1909.gz
# Folder - Year
# .tag.gz files within a year folder - <station_id>-<year>.tar.gz - 028060-99999-1909.gz
# 
# We want a file with a specific Id for these years range

import os
from ftplib import FTP, error_perm

def ftpDownloader(stationId, startYear, endYear, url='ftp.pyclass.com', user='student@pyclass.com', passwd='student123'):
    ftp=FTP(url)
    ftp.login(user, passwd)
    if not os.path.exists('./in'):
        os.makedirs('./in') # Should create a in folder if it doesn't exist
    os.chdir('./in')

    for year in range(startYear, endYear+1):
        #fullPath='/Data/year/stationId-year.gz'
        fullPath='/Data/%s/%s-%s.gz' %(year,stationId,year)
        filename=os.path.basename(fullPath)     # Local File name
        try:
            with open(filename, 'wb') as file:
                ftp.retrbinary('RETR %s' %fullPath, file.write)
            print('%s successfully downloaded' %filename)
        except error_perm:
            print('%s is not available' % filename)
            os.remove(filename) # If the remote file does not exist, empty file created in the with will be deleted here. 
    ftp.close()

ftpDownloader('010010-99999', 2010, 2014)


## Additional steps

ids=['010010-99999', '010014-99999']

for name in ids:
    ftpDownloader(name, 2010, 2014)  # This function will be excuted 2 times 
    

