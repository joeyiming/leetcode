#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    SYMBOL_VALUES = [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1),
    ]


    def romanToInt(self,s: str) -> int:
        ans = 0
        while s:
            for symbol, value in Solution.SYMBOL_VALUES:
                # print(s)
                # print(symbol)
                if s.startswith(symbol):
                    # print(value)
                    # print(ans)
                    ans += value
                    s = s[len(symbol):]
        return ans
# @lc code=end

