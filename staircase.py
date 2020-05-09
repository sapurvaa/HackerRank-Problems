#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        space = ""
        hash_char = ""
        for j in range(n-i-1):
            space = space + " "
        for k in range(i+1):
            hash_char = hash_char + "#"
        print(space+hash_char)

if __name__ == '__main__':
    n = int(input())

    staircase(n)
