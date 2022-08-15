#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#include <set>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	long long n = 0, m = 0;
	cin >> n >> m;
	n -= 1;
	int c = 0;
	if (n <= 3) {
		cout << 1;
		return 0;
	}
	if (m == 1) {
		cout << 0;
		return 0;
	}
	vector<int> nums(3,1);
	for (int i = 3; i <m*m*m; i++) {
		nums.push_back((nums[i - 1] + nums[i - 2] + nums[i - 3]) % m);
		if (nums[i] == 1)
			c++;
		else
			c = 0;
		if (c == 3) {
			n %= (i - 2);
			break;
		}
	}
	cout << nums[n];
}