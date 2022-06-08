#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self,s: str) -> str:
        result = s[0]
        center = 0
    
        # 判断偶数回文串
        while center <= len(s):
            left = center - 1
            right = center
            print(f'left:{left},right:{right}')
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right+1-left > len(result):
                    result = s[left:right+1]
                left -= 1
                right += 1
            center += 1
    
        print(f'result: {result}')
    
        # 判断奇数回文串
        maxHalfLen = 1
        center = 0
        while center <= len(s):
            left = center - 1
            right = center + 1
            # print(f'left:{left},right:{right}')
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right+1-left > len(result):
                    result = s[left:right+1]
                    # print(f'result: {result}')
                left -= 1
                right += 1
            center += 1
    
        print(f'result: {result}')
        return result
# @lc code=end
