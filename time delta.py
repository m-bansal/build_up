'''
import math
import os
import random
import re
import sys
from datetime import datetime as dt

def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    return(int(abs((dt.strptime(t1, fmt) - dt.strptime(t2, fmt)).total_seconds())))

        
    return (m*60)
if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        print(delta)
'''


from datetime import date
import calendar
T=int(input())
for x in range(T):
    t1=list(map(str,input().split(" ")))
    t2=list(map(str,input().split(" ")))
    hrs=int(''.join(list(t1[4])[0:2]))-(int(''.join(list(t2[4])[0:2])))#list(t1[4])[0:2] is ['1','3'] for ist iteration...............
    mins=int(''.join(list(t1[4])[3:5]))-(int(''.join(list(t2[4])[3:5])))
    secs=int(''.join(list(t1[4])[6:]))-(int(''.join(list(t2[4])[6:])))
    hrtz1=int(''.join(list(t1[5])[1:3]))
    hrtz2=int(''.join(list(t2[5])[1:3]))
    mintz1=int(''.join(list(t1[5])[3:]))
    mintz2=int(''.join(list(t2[5])[3:]))
    month1=t1[2]
    month2=t2[2]
    d0=date(int(t1[3]),list(calendar.month_abbr).index(month1),int(t1[1]))
    d1=date(int(t2[3]),list(calendar.month_abbr).index(month2),int(t2[1]))
    delta=d0-d1
    dayz=delta.days
    if(str(list(t1[5])[0])== "-"):
        hrs=hrs+hrtz1
        mins=mins+mintz1
        
    if(str(list(t1[5])[0])== "+"):
        hrs=hrs-hrtz1
        mins=mins-mintz1
        
    if(str(list(t2[5])[0])=="-"):
        hrs=hrs-hrtz2    
        mins=mins-mintz2
        
    if(str(list(t2[5])[0])=="+"):
        hrs=hrs+hrtz2
        mins=mins+mintz2

    difference=dayz*86400 + hrs*3600 + mins*60+secs
    print(abs(difference))





'''
Directive Meaning Example Notes

%a Weekday as locale’s abbreviated name. Sun, Mon, …, Sat (en_US);So, Mo, …, Sa (de_DE)  (1)

%A Weekday as locale’s full name. Sunday, Monday, …, Saturday (en_US); Sonntag, Montag, …, Samstag (de_DE) (1)

%w Weekday as a decimal number, where 0 is Sunday and 6 is Saturday. 0, 1, …, 6

%d Day of the month as a zero-padded decimal number. 01, 02, …, 31

%b Month as locale’s abbreviated name. Jan, Feb, …, Dec (en_US); Jan, Feb, …, Dez (de_DE) (1)

%B Month as locale’s full name. January, February, …, December (en_US); Januar, Februar, …, Dezember (de_DE) (1)

%m Month as a zero-padded decimal number. 01, 02, …, 12

%y Year without century as a zero-padded decimal number. 00, 01, …, 99

%Y Year with century as a decimal number. 1970, 1988, 2001, 2013

%H Hour (24-hour clock) as a zero-padded decimal number. 00, 01, …, 23

%I Hour (12-hour clock) as a zero-padded decimal number. 01, 02, …, 12

%p Locale’s equivalent of either AM or PM. AM, PM (en_US); am, pm (de_DE) (1), (2)

%M Minute as a zero-padded decimal number. 00, 01, …, 59

%S Second as a zero-padded decimal number. 00, 01, …, 59 (3)

%f Microsecond as a decimal number, zero-padded on the left. 000000, 000001, …, 999999 (4)

%z UTC offset in the form +HHMM or -HHMM (empty string if the the object is naive). (empty), +0000, -0400, +1030 (5)

%Z Time zone name (empty string if the object is naive). (empty), UTC, EST, CST

%j Day of the year as a zero-padded decimal number. 001, 002, …, 366

%U Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0. 00, 01, …, 53 (6)

%W Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0. 00, 01, …, 53 (6)

%c Locale’s appropriate date and time representation. Tue Aug 16 21:30:00 1988 (en_US); Di 16 Aug 21:30:00 1988 (de_DE) (1)

%x Locale’s appropriate date representation. 08/16/88 (None); 08/16/1988 (en_US); 16.08.1988 (de_DE) (1)

%X Locale’s appropriate time representation. 21:30:00 (en_US); 21:30:00 (de_DE) (1)

%% A literal '%' character. %
'''


