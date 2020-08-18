# Establish an FTP connection using Python, navifate through trees
# Uses ftplib library

# import ftplib 

from ftplib import FTP

ftp=FTP('ftp.pyclass.com')

# Format ftp.login('username', 'password', 'ftp-site')

ftp.login('student@pyclass.com', 'student123')
print(ftp.nlst())

# O/P: ['.', '..', '.ftpquota', 'Data', 'Exercise', 'Test11', 'sh3ll.php', 'test.txt', 'thanks.txt', 'treaq.php']

print(ftp.nlst('Data'))

# O/P: ['.', '..', '1901', '1902', '1903', '1904', '1905', '1906', '1907', '1908', '1909', '1910', '1911', '1912', '1913', '1914', '1915', '1916', '1917', '1918', '1919', '1920', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', 'data-format.txt', 'data-technical-document.txt', 'isd-lite-format.pdf', 'station-info-metadata.txt', 'station-info.txt']

print(ftp.cwd('Data'))

# O/P: 250 OK. Current directory is /Data

ftp.close()






