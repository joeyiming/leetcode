#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        strInt = str(x)
        if strInt==strInt[::-1]:
            return True
        else:
            return False
# @lc code=end

