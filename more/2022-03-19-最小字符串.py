def judge(a,b):
    return a+b > b+a

def getMinStr(l:list)->str:
    '''冒泡'''
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if judge(l[i],l[j]):
                l[i],l[j] = l[j],l[i]
    return ''.join(l)
# ? 快排解法
# def getMinStr(l:list)->str:
#     '''快排'''
#     def part(l,left,right):


#     def qsort(l:list,left,right):
#         mid = (left+right)//2
#         if left<right:
#             qsort(l,left,mid-1)
#             qsort(l,mid+1,right)
#     qsort(l,0,len(l))
#     return ''.join(l)


t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    cur = []
    for _ in range(n):
        cur.append(input().strip())
    ans.append(getMinStr(cur))
for i in range(t):
    print(ans[i])

'''
babababbabb
bababbb
babbbb
aabac
aababcbbcbacbaac
aaacd
aacab
abcbd
aabac
abac
babd
'''
