'''Alex works at a clothing store. There is a large pile of socks that must be paired by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are n=7 socks with colors [1,2,1,1,1,3,2], which would be 3 pairs of socks. 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict

def sockMerchant(n, ar):
    
    sox = defaultdict(int)
    for s in ar:
        sox[s] += 1
        
    pairs_count = 0
    for ele in sox.values():
        pairs_count += ele//2
    
    return(pairs_count)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')
    fptr.close()

