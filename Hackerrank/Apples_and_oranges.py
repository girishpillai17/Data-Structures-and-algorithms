#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    counta = 0
    for i in apples:
        if s <= i+a <= t:
            counta += 1
        else:
            counta == counta
    
    countb = 0
    for j in oranges:
        if  s <= j+b <= t:
            countb += 1
        else:
            countb == countb
        
    print(counta)
    print(countb)

if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)


//test commit
