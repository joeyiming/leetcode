var reverse = function (x) {
  const MIN = Math.pow(-2, 31);
	const MAX = Math.pow(2, 31) - 1;
	if (x == 0) {
		return 0;
	}
	let first = x;
	let result = 0;
	while (x / 10) {
		first = parseInt(x % 10);
		x = parseInt(x / 10);
		result = result * 10 + first;
	}
	return (result>MIN&&result<MAX)?result:0;
};

// reverse(123);
console.log(reverse(120));
console.log(reverse(1534236469));
console.log(reverse(-1));

// var reverse = function (x) {
// 	let rev = 0;
// 	while (x !== 0) {
// 		const digit = x % 10;
// 		// ~~ 是两次按位非操作，效果同Math.trunc，舍弃小数部分
// 		x = ~~(x / 10);
// 		rev = rev * 10 + digit;
// 		if (rev < Math.pow(-2, 31) || rev > Math.pow(2, 31) - 1) {
// 			return 0;
// 		}
// 	}
// 	return rev;
// };