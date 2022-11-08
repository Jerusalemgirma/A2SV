#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    count = 0
    for i in range(len(a)):
        for j in range(len(a)- 1):
            if (a[j] > a[j + 1]):
                s = a[j]
                a[j] = a[j+1]
                a[j + 1] = s
                count += 1
        
        a, swapcount = 0, 0
    while True:
        swapped = False
        for i in range(1, len(a)):
            a += 1
            if a[i-1] > a[i]:
                swapcount += 1
                a[i-1], a[i] = a[i], a[i-1]
                swapped = True
        if not swapped:
            break
    return a, swapcount

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
