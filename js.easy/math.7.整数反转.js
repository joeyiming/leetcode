/*
 * @lc app=leetcode.cn id=7 lang=javascript
 *
 * [7] 整数反转
 */

// @lc code=start
/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  const MIN = Math.pow(-2, 31);
	const MAX = Math.pow(2, 31) - 1;
	if (x == 0) {
		return 0;
	}
	let first = x;
	let result = 0;
	while (x / 10) {
		first = x % 10;
		x = parseInt(x / 10);
		result = result * 10 + first;
	}
	return (result>MIN&&result<MAX)?result:0;
};
// @lc code=end

