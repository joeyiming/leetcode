# 求解函数
def getCount(num):
    k = len(str(num))-3
    if num < 520*(10**k):
        k = k - 1
    max520 = 520*(10**k)
    print(f'{max520=}')
    if num<520:
        return 0
    else:
        return getCount(num-max520)+1
    


# 输入
T = int(input())
for i in range(T):
    num = int(input())
    if num<520:
        print(-1)
    else:
        print(getCount(num))
