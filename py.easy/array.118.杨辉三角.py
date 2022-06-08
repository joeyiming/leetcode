#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
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
    
class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        # 从1开始计数
        for i in range(1, numRows+1):
            ans.append(getRow(i))
        return ans    
# @lc code=end

