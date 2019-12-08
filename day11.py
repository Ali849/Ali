#!/bin/python3

import math
import os
import random
import re
import sys
#__________________________MY SOLUTION___________________________

if __name__ == '__main__':
  arr = []
  all=[]
  result=[]
  for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
  count=0
  i=0
  while i <5:
    x=[]
    x.append(arr[count][i:i+3])
    x.append(arr[count+1][i+1])
    x.append(arr[count+2][i:i+3])
    all.append(x)
    i+=1
    if i ==4:
      count+=1
      i-=4
    if count==4:
      break
  for f in range(0,16):
    sum1=sum(all[f][0])+all[f][1]+sum(all[f][2])
    result.append(sum1)
  print(max(result))
