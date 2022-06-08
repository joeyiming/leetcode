#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = 0
        maxLenOfSub = 0
        length = len(s)
        while (cur < length-maxLenOfSub):
            charSet = set()
            for i in s[cur:]:
                if (i not in charSet):
                    charSet.add(i)
                else:
                    break
            # print(charSet)
            if len(charSet) > maxLenOfSub:
                maxLenOfSub = len(charSet)
            cur += 1

        return maxLenOfSub
# @lc code=end

