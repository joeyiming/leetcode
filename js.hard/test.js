function titleCase(str) {
	let array = str.split(' ');
	let result = [];
	for (let i = 0; i < array.length; i++) {
		let tem = '';
		tem = array[i].charAt(0).toUpperCase() + array[i].substring(1);
		result.push(tem);
	}
  str = result.join(' ');
	return str;
}

console.log(titleCase("I'm a little tea pot")); 

