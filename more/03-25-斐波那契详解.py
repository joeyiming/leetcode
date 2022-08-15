# def fib(n):
#     if n == 0: return 0
#     if n == 1: return 1
#     return fib(n-1)+fib(n-2)

def fib(n, memo=None):
    if n == 0 or n == 1: return n
    if not memo:
        return fib(n, [0]*(n+1))
    elif memo[i] == 0:
        return fib(n-1, memo)+fib(n-2, memo)

# def fib(n):
#     if n == 0 or n == 1: return n
#     memo = [0, 1]
#     for i in range(2, n+1):
#         memo.append(memo[i-1]+memo[i-2])
#     return memo[n]


# def fib(n):
#     if n == 0 or n == 1: return n
#     a, b = 0, 1
#     for _ in range(2, n+1):
#         a, b = b, a+b
#     return b


for i in range(8):
    print(fib(i))
