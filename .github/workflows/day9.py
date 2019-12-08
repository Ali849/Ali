#!/bin/python3

import math
import os
import random
import re
import sys
def factorial(n):
  y=1
  while n>0:
    y*=n
    n-=1
    if n==1:
      return(y)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
