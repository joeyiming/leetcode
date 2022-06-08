#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self,s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        route = numRows*2-2
        strList = [""]*numRows
        for index, char in enumerate(s):
            strPos = index % route
            listPos = min(strPos, route-strPos)
            strList[listPos] += char
    
        ans = ""
        for i in strList:
            ans += i
        return ans
# @lc code=end

