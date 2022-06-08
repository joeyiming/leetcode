# 逐一添加砝码，每加一个砝码对原状态进行更新
n = int(input())
nums=input()
nums=list(map(int,nums.split()))
nums.sort()
ans = set()

for i in range(len(nums)):
    tem=set()
    tem.add(nums[i])
    for j in ans:
        tem.add(abs(nums[i]+j))
        if nums[i]!=j:
            tem.add(abs(nums[i]-j))
    ans=ans | tem
print(len(ans))
