from datetime import date

dateNum = 19300600
while True:
  dateNum+=1
  # print(dateNum)
  dateStr = str(dateNum)
  try:
     date(int(dateStr[:4]),int(dateStr[4:6]),int(dateStr[6:8]))
  except:
    continue
  else:
    # print(dateNum)
    if dateNum % 6036 == 0 and int(dateStr[4:6])==6:
      print(dateNum)
      break

# 19550604
