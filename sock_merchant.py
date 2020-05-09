#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    colour = {}
    for i in ar:
        if i in colour:
            colour[i] += 1
        else:
            colour[i] = 1
    
    v = colour.values()
    for val in v:
        pairs = pairs + val//2
    
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
