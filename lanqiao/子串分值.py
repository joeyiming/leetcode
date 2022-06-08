import os
import sys

# 请在此输入您的代码
word = input()

# 暴力法
# for i in range(1,length+1):
#   if i==1:
#     ans+=length
#     continue
#   subLen = i
#   for startPos in range(length-subLen):
#     pass


# 递归法
def countSingleChar(string):
  charSet = set(string)
  count = 0
  for char in charSet:
    if string.count(char) == 1:
      count+=1
  return count
  

def countRecursion(string):
  length = len(string)
  if length==1:
    return 1
  else:
    remainCount = 0
    for i in range(1,length+1):
      remainCount+=countSingleChar(string[-i:])
    return countRecursion(string[:-1])+remainCount

print(countRecursion(word))
