#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
#

# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        MAXVALUE = float('inf')

        def dfs(grid, i, j, length, queue):
            print(i, j, queue, length)
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 0 or [i, j] in queue:
                return MAXVALUE
            if i == len(grid)-1 and j == len(grid[0])-1:
                queue = [[0, 0]]
                return length+1
            queue.append([i, j])
            return min(
                dfs(grid, i+1, j+1, length+1, queue),
                dfs(grid, i+1, j, length+1, queue),
                dfs(grid, i+1, j-1, length+1, queue),
                dfs(grid, i-1, j+1, length+1, queue),
                dfs(grid, i-1, j, length+1, queue),
                dfs(grid, i-1, j-1, length+1, queue),
                dfs(grid, i, j+1, length+1, queue),
                dfs(grid, i, j-1, length+1, queue))
        queue = []
        result = dfs(grid, 0, 0, 0, queue)
        return result if result != MAXVALUE else -1

# @lc code=end

