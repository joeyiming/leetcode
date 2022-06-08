#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            length = len(nums)
            ans = []
            if length < 3:
                return ans

            # 去重手段一：排序
            nums.sort()
            # print(nums)

            for i in range(length):
                # 去重手段二：更新后的元素不能和上一个元素相同
                if i == 0 or nums[i] != nums[i-1]:
                    k = length-1
                    for j in range(i+1, length):
                        # 去重手段三:保证a<=b<=c 即 i<j<k
                        # print(i, j, k)
                        if j == i+1 or nums[j] != nums[j-1]:
                            while j < k and nums[i]+nums[j]+nums[k] >= 0:
                                if k == length-1 or nums[k] != nums[k+1]:
                                    if nums[i]+nums[j]+nums[k] == 0:
                                        # print(i, j, k)
                                        ans += [[nums[i], nums[j], nums[k]]]
                                k -= 1

            return ans
# @lc code=end
