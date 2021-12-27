
import re

pattern = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
mo1 = pattern.findall('33/03/2003 and 04/09/2001')

for i in range(len(mo1)):

    x = list(mo1[i])
    nday = 0
    nmonth = 0
    nyear = 0

    leap_year = (int(x[2]) % 4 == 0 and int(x[2]) % 100 != 0) or (int(x[2]) % 4 == 0 and int(x[2]) % 100 == 0 and int(x[2]) % 400 == 0)
    if int(x[0]) not in range(1,32):
        nday = 0
        
    else: 
        nday = 1

    if int(x[1]) not in range(1,13):
        nmonth = 0
    else: 
        nmonth = 1

    if int(x[2]) not in range(1000,3000):
        nyear = 0
    else: 
        nyear = 1

    if (nday and (nmonth and nyear)) == 1:
        print("This date is a valid date")
    else:
        print("This is not a valid date")
#print('/'.join(x))




