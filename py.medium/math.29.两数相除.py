#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def multiply(a, b):
        '''用加法替代乘法'''
        sum = 0
        for i in range(abs(b)):
            sum += a
        if b > 0:
            return sum
        else:
            return -sum

    def divide(self, dividend: int, divisor: int) -> int:
        '''用乘法替代除法'''
        min = -2**31
        max = 2**31-1

        # 先当作两个正数相除，最后再判断商的正负性
        ans = abs(dividend)
        while ans > 0:
            if ans*abs(divisor) <= abs(dividend):
                # print(ans)
                break
            ans -= 1

        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            pass
        else:
            ans = -ans

        if ans >= min and ans <= max:
            return ans
        else:
            return max


# @lc code=end
