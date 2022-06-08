import os
import sys

# 请在此输入您的代码
word = input()
word = sorted(word,reverse=True)
charDict = {}
for char in word:
  if char not in charDict:
    charDict[char] = 1
  else:
    charDict[char]+=1
# print(charDict)

maxChar = ''
maxCount = 0
for char,count in charDict.items():
  if count>maxCount:
    maxChar = char
    maxCount = count
  
print(maxChar)
print(maxCount)
