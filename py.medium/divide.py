import math
# 目的效果
# def divide(self, dividend: int, divisor: int) -> int:
#     min = -2**31
#     max = 2**31-1
#     ans = math.trunc(dividend/divisor)
#     if ans >= min and ans <= max:
#         return math.trunc(dividend/divisor)
#     else:
#         return max
# 要求：不使用乘法除法取余
# 基本思路：用加法替代乘法，乘法替代除法

# 朴素算法，效率过低


def divide(dividend: int, divisor: int) -> int:
    '''用乘法替代除法'''
    min = -2**31
    max = 2**31-1

    # 先当作两个正数相除，最后再判断商的正负性
    ans = abs(dividend)
    print('i', ans)
    while ans > 0:
        # print('a',ans)
        if ans*abs(divisor) <= abs(dividend):
            # print('ans ',ans)
            break
        # print('b',ans)
        ans -= 1

    # print('c',ans)
    if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
        pass
    else:
        ans = -ans

    if ans >= min and ans <= max:
        return ans
    else:
        return max


def multiply(a, b):
    '''用加法替代乘法'''
    sum = 0
    for i in range(abs(b)):
        sum += a
    if b > 0:
        return sum
    else:
        return -sum


if __name__ == '__main__':
    # test1 = -1
    test1 = 2147483647
    # test2 = 1
    test2 = 2
    print("test:", test1, ' ', test2)
    # print(isPalindrome(test1))
    print(divide(test1, test2))
    # print(multiply(test1, test2))
    # print(convert('A',1))

'''
10 / 3 = 3 ······ 1
3 * 3 < 10 
3 * 4 > 10
ans = 3

7 / -3 = -2 ······ 1
-3 * -2 = 6 < 7
-3 * -3 = 9 > 7
ans = -2

3 * 3 = 3 + 3 +3
'''
