
import math
import os
import random
import re
import sys
import datetime
import calendar

def time_to_second(t):
    multi = 1
    mon = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12 }
    day, dd, mn, yyyy, hms, tz = t.split()
    hh, mm, ss = hms.split(':')
    d1 = datetime.datetime(int(yyyy), mon[mn], int(dd), int(hh), int(mm), int(ss))
    d2 = calendar.timegm(d1.timetuple())
    if tz[0] == '-':
        multi = 1
    else:
        multi = -1
    tz1 = int(tz[1:3])
    tz2 = int(tz[3:])

    adjust = ((tz1 * 60) + tz2) * 60 * multi
    d2 += adjust
    return d2


# Complete the time_delta function below.
def time_delta(t1, t2):

    s1 = time_to_second(t1)
    s2 = time_to_second(t2)

    return abs(s1-s2)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)
        print(delta)
        #fptr.write(delta + '\n')

    #fptr.close()