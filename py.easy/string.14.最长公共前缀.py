#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 2:
            return strs[0]
            
        # a是前两个字符串中较短的那个，b相反
        a = strs[0] if len(strs[0]) < len(strs[1]) else strs[1]
        b = strs[1] if len(strs[0]) < len(strs[1]) else strs[0]
        ans = ""
        for index, char in enumerate(a):
            if char == b[index]:
                ans += char
            else:
                break

        if len(strs) < 3:
            return ans
        else:
            return Solution.longestCommonPrefix(Solution,[ans]+strs[2:])
# @lc code=end
