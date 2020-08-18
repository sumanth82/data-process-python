from ftplib import FTP
import os

def ftpDownloader(host, user, passwd):
    ftp=FTP(host)
    ftp.login(user, passwd)
    ftp.cwd('Data')
    os.chdir('./')
    with open('isd-lite-format.pdf', 'wb') as file:
        ftp.retrbinary('RETR isd-lite-format.pdf', file.write)      # retrbinary - Retrieve Binary method of ftp # Retrieves the pdf file to the pwd
    

ftpDownloader('ftp.pyclass.com', 'student@pyclass.com', 'student123')


#### Optimize the above code -- See below####


def ftpDownloader(filename, host='ftp.pyclass.com', user='student@pyclass.com', passwd='student123'):
    ftp=FTP(host)
    ftp.login(user, passwd)
    ftp.cwd('Data')
    os.chdir('./')
    with open(filename, 'wb') as file:
        ftp.retrbinary('RETR %s' %filename, file.write)      # retrbinary - Retrieve Binary method of ftp # Retrieves the pdf file to the pwd
    
ftpDownloader('isd-lite-format.pdf')
