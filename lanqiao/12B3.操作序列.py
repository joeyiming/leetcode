def downSortToIndex(index:int):
    global initList
    initList = sorted(initList[:index],reverse=True)+initList[index:]

def upSortFromIndex(index:int):
    global initList
    initList = initList[:index-1]+sorted(initList[index-1:])

def getAns(m: int):
    for i in range(m):
        inputStr = input().split()
        flag = int(inputStr[0])  # 操作类型
        index = int(inputStr[1])  # 参数
        if flag==0:
            downSortToIndex(index)
        else:
            upSortFromIndex(index)

# 样例操作
# initList = [i for i in range(1,4)]
# print(*initList)
# downSortToIndex(3)
# print(initList)
# upSortFromIndex(2)
# print(initList)
# downSortToIndex(2)
# print(initList)

# 主过程
inputStr = input().split()
n = int(inputStr[0]) # 序列长度
m = int(inputStr[1]) # 操作次数
initList = [i for i in range(1,n+1)]
getAns(m)
print(*initList)
