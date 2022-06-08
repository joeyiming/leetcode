# 杨辉三角形【第十二届】【省赛】【B组】

# 根据行数获取该行的最大数
# getRowMax(5) = 6
def getRowMax(row: int):
    if row < 2:
        return 1
    if row % 2 == 1:
        return getRowMax(row-1) * 2
    else:
        pass


# 根据行数获取该行第一个数的总序号
# getRowIndex(5) = 11
def getRowIndex(row: int):
    if row == 1:
        return 1
    else:
        return getRowIndex(row-1)+(row-1)


# 根据行数获取该行的杨辉三角数
# getRow(5) = [1,4,6,4,1]
def getRow(row: int):
    if row == 1:
        return [1]
    if row == 2:
        return [1, 1]
    lastRow = getRow(row-1)
    thisLen = len(lastRow)+1
    thisRow = [0]*thisLen
    # 构造当前行，当前行的长度为上一行的长度加一
    for i in range(len(lastRow)+1):
        # 首尾为1
        if i == 0 or i == len(lastRow):
            thisRow[i] = 1
        else:
            thisRow[i] = lastRow[i-1]+lastRow[i]
    return thisRow

# 求解答案


def getAns(N: int):
    ans = 1
    if N < 2:
        return ans

    row = 1
    AnsNotFound = True
    while (AnsNotFound):
        for index, value in enumerate(getRow(row)):
            if value == N:
                AnsNotFound = False
                ans = getRowIndex(row) + index
                return ans
        row += 1


if __name__ == "__main__":
    # print(getRowIndex(5))
    n = int(input())
    print(getAns(n))
