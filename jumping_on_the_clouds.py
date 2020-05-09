#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count = 0
    step = 0
    while step < len(c)-1:
        if step == len(c)-2:
            step += 1
            count += 1 
        elif c[step] == 0 and c[step+2] == 0:
            step += 2
            count += 1
        elif c[step] == 0 and c[step+2] == 1:
            step += 1
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
