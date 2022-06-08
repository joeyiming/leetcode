import os
import sys
from math import *
# 请在此输入您的代码
order = 3
num = 5

def isPrime(num):
  for i in range(2,round(sqrt(num))+1):
    # print(num,i)
    if num % i == 0:
      # print(num)
      return False
  return True

while True:
  num+=1
  if isPrime(num):
    order+=1
    if order==2019:
      print(num)
      break
