num = []
numRow = int(input())  # 输入数据
for i in range(numRow):
    num.append(list(map(int, input().split())))
dp = []
for i in range(numRow):
    dp.append([0]*numRow)
dp[0][0] = num[0][0]

for i in range(1, numRow):
    # 初始化边界
    dp[i][0] = dp[i-1][0] + num[i][0]
    dp[i][i] = dp[i-1][i-1] + num[i][i]

for i in range(1, numRow):
    for j in range(1, numRow):
        if j < i:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])+num[i][j]  # 状态转移函数

# 判断奇偶
if numRow % 2 == 0:
    print(max(dp[numRow-1][numRow//2], dp[numRow-1][numRow//2-1]))
if numRow % 2 != 0:
    print(dp[numRow-1][(numRow-1)//2])


# yl:
# numRow = 5
# numList = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

# lTimes = rTimes = 0
# total = numList[0][0]
# for i in range(numRow-2):
#   print(f'循环开始：{i=},{lTimes=},{rTimes=},{total=}')

#   if numRow-lTimes != lTimes and numRow-lTimes-1 != lTimes and numRow-rTimes-1 != rTimes:
#     print('左边大于右边')
#     if numList[i+1][i] > numList[i+1][i+1]:
#       lTimes += 1
#       total += numList[i+1][i]
#     else:
#       rTimes += 1
#       total += numList[i+1][i+1]

#   if numRow % 2 == 0 and numRow-lTimes == lTimes:
#     print('情况一')
#     temp = i
#     for j in range(lTimes):
#       total += numList[temp+1][1+temp]
#       temp += 1

#   if numRow % 2 != 0 and numRow-lTimes-1 == lTimes:
#     print('情况二')
#     temp = i
#     for j in range(lTimes-1):
#       total += numList[temp+1][temp]
#       temp += 1

#   if numRow % 2 != 0 and numRow-rTimes-1 == rTimes:
#     print('情况三')
#     temp = i
#     for j in range(rTimes-1):
#       total += numList[temp+1][temp+1]
#       temp += 1

#   print(f'循环结束：{i=},{lTimes=},{rTimes=},{total=}')

# print(total)
