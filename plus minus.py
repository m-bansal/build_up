import math
import os
import random
import re
import sys
def plusMinus(arr):
    p=0
    n=0
    z=0
    l=len(arr)
    for i in arr:
        if i>0:
            p+=1
        elif i<0:
            n+=1
        else:
            z+=1
    print('{:.6f}'.format( p/l))
    print('{:.6f}'.format( n/l))
    print('{:.6f}'.format( z/l))    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
