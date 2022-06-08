#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return Solution.climbStairs(Solution, n-1)+Solution.climbStairs(Solution, n-2)

if __name__ == '__main__':
    print(Solution.climbStairs(Solution,40))
# @lc code=end

