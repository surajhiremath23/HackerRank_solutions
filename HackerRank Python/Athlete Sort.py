# n, m = map(int, input().split())
# nums = [list(map(int, input().split())) for i in range(n)]
# k = int(input())

# nums.sort(key=lambda x: x[k])

# for line in nums:
#     print(*line, sep=' ')

# alternative solution

#!/bin/python3

import math
import os
import random
import re
import sys
if __name__ == '__main__':
    nm = input().split()
    r = int(nm[0])
    c = int(nm[1])
    arr = []

    for _ in range(r):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    for i in range(r):
        arr[i][0],arr[i][k]=arr[i][k],arr[i][0]

    arr=sorted(arr)
    
    for i in range(r):
        arr[i][k],arr[i][0]=arr[i][0],arr[i][k]
        
    for line in (arr):
        print(*line)

    

