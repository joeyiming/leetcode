# 运行错误	20

def getsum(row):
    return (1+row)*row//2


def getrow(n):
    # 行数从 0 开始计数
    row = [1]*(n+1)
    for i in range(1, n):
        row[i] = row[i-1]*(n-i+1)//i
    return row


def findrow(n, l, r):
    # 二分法
    mid = (l + r)//2
    if row_mem[mid-1][0] == 0:
        row_mem[mid-1] = getrow(mid-1)
    if row_mem[mid][0] == 0:
        row_mem[mid] = getrow(mid)
    low, high = max(row_mem[mid-1]), max(row_mem[mid])
    # * DEBUG
    # print(f'{n=},{mid=},{low=},{high=}')
    if n == low:
        return mid-1
    if n <= high and n > low:
        return mid
    elif n < low:
        return findrow(n, l, mid-1)
    else:
        return findrow(n, mid+1, r)

n = int(input().strip())
row_mem = [[0]]*31
if n == 1:
    print(1)
elif n <= 10:
    row = findrow(n, 0, 5)
else:
    row = findrow(n, 0, 30)
while row_mem[row].count(n) < 1:
    row+=1
    if row_mem[row][0]==0:
        row_mem[row] = getrow(row)
else:
    # * DEBUG
    # print(f'{row=}')
    print(f'{row_mem[row]}')
    print(getsum(row)+row_mem[row].index(n)+1)
