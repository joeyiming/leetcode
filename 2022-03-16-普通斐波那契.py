def fib(n):
    '''递归求斐波那契数列'''
    return 1 if n<2 else fib(n-1) + fib(n-2)

def climbStairs(n: int) -> int:
    '''迭代'''
    if n<2:
        return n
    dp = [1,2]
    # 约定俗成: 当迭代用的 i 不在循环体中使用时，可用 _ 代替（不改变程序含义）
    for _ in range(3,n+1):
        dp[0],dp[1] = dp[1],dp[0]+dp[1]
    return dp[1]

print('斐波那契数列：',[fib(x) for x in range(10)])
print('爬楼梯数列：', [climbStairs(x) for x in range(10)])
# 运行结果：
# 斐波那契数列： [1, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# 爬楼梯数列： [0, 1, 2, 3, 5, 8, 13, 21, 34, 55]