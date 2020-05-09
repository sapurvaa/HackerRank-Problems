#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    plus_ratio,minus_ratio,zero_ratio = 0.0,0.0,0.0
    for i in arr:
        if i > 0:
            plus_ratio += 1
        elif i < 0:
            minus_ratio += 1
        else:
            zero_ratio += 1
    print(round(plus_ratio/len(arr),6))
    print(round(minus_ratio/len(arr),6))
    print(round(zero_ratio/len(arr),6))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
