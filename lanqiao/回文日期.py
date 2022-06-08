import os
import sys
from datetime import date
# 请在此输入您的代码
startDate = input()
startYear = startDate[:4]
startMonth = startDate[4:6]
startDat = startDate[6:8]
endYear = '8999'
firstFound = False
ababFound = False

for yearNum in range(int(startYear),int(endYear)+100):
  year = str(yearNum)
  newDate = year+year[::-1]
  month = newDate[4:6]
  day = newDate[6:8]
  try:
    # 使用datetime库检查日期合法性
    date(int(year),int(month),int(day))
  except:
    continue
  else:
    if firstFound and ababFound:
      break
    if date(int(year),int(month),int(day)) < date(int(startYear),int(startMonth),int(startMonth)):
      continue
    if not firstFound:
      print(newDate)
      firstFound = True
    # ABAB
    if year[0]!=year[1] and year[0]==year[2] and year[1]==year[3]:
      print(newDate)
      ababFound = True
    
