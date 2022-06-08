#
# @lc app=leetcode.cn id=1219 lang=python3
#
# [1219] 黄金矿工
#

# @lc code=start
class Solution:
    def dfs(self, grid: list, i, j, nums):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return nums
        nums += grid[i][j]
        # print(i,j,nums)
        tem = grid[i][j]
        grid[i][j] = 0
        up = self.dfs(grid, i-1, j, nums)
        down = self.dfs(grid, i+1, j, nums)
        left = self.dfs(grid, i, j-1, nums)
        right = self.dfs(grid, i, j+1, nums)
        grid[i][j] = tem
        return max(up, down, left, right)

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        maxsofar = 0
        for i in range(len(grid)):
            if grid[i].count(0) == len(grid[i]):
                continue
            else:
                for j in range(len(grid[i])):
                    if j != 0:
                        maxsofar = max(self.dfs(grid, i, j, 0), maxsofar)
        return maxsofar
# @lc code=end
