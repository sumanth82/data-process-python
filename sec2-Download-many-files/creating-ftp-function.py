from ftplib import FTP

def ftpDownloader(host, user, passwd):
    ftp=FTP(host)
    ftp.login(user, passwd)
    print(ftp.nlst())
    # O/P: ['.', '..', '.ftpquota', 'Data', 'Exercise', 'Test11', 'sh3ll.php', 'test.txt', 'thanks.txt', 'treaq.php']

ftpDownloader('ftp.pyclass.com', 'student@pyclass.com', 'student123')
