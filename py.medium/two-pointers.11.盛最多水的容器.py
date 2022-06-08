#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        i = 0
        j = len(height)-1
        while i <= j:
            # 计算容积
            h = min(height[i], height[j])
            w = j-i
            area = h * w
    
            if maxArea < area:
                maxArea = area
    
            # 更新较小高度所在的指针
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
    
        return maxArea
# @lc code=end

