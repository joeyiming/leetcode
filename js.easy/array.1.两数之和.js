/*
 * @lc app=leetcode.cn id=1 lang=javascript
 *
 * [1] 两数之和
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  for(let i=0;i<nums.length;i++){
    let a = nums[i];
    for(let j=i+1;j<nums.length;j++){
      let b =nums[j];
      if(a+b===target){
        return [i,j];
      }
    }
  }
};
// @lc code=end

// 暴力求解
// var twoSum = function (nums, target) {
// 	for (let i = 0; i < nums.length; i++) {
// 		let a = nums[i];
// 		for (let j = i + 1; j < nums.length; j++) {
// 			let b = nums[j];
// 			if (a + b === target) {
// 				return [i, j];
// 			}
// 		}
// 	}
// };
