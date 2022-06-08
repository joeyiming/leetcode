#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
import re


class Solution:
    def myAtoi(self, s: str) -> int:
        min = -2**31
        max = 2**31-1
        numRegex = re.compile(r'^[+-]?\d+')
        match = numRegex.search(s.lstrip())
        if match:
            numStr = match.group()
        else:
            numStr = '0'
        ans = int(numStr)
        return ans if ans > min and ans < max else min if ans < max else max


# @lc code=end
