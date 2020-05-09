#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    if 'PM' in s and s[:2] != '12':
        h = str(int(s[:2]) + 12)
        return h+s[2:8]
    else:
        if s[:2] == '12' and 'AM' in s:
            return '00'+s[2:8]
        else:
            return s[:8]
    #

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
