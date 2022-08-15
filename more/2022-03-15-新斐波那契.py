# 正确	100

n, m = map(int, input().strip().split())

if m == 1:
    print(0)
elif n <= 3:
    print(1)
else:
    results = [1]*3
    T = 0
    cnt = 0
    for i in range(3, m*m*m):
        results.append((results[i-1]+results[i-2]+results[i-3]) % m)
        if results[i] == 1:
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            T = i - 2
            break
    print(results[n % T - 1])
