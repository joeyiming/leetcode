#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
import math
class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        while(x != 0):
            if (x >= 0):
                first = x % 10
            else:
                first = x % 10 - 10
                if (first == -10):
                    first = 0
            x = math.trunc(x/10)
            result = result*10 + first
        MIN = -2**31
        MAX = 2**31-1
        return result if result > MIN and result < MAX else 0
# @lc code=end
