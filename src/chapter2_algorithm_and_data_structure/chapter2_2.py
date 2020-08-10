'''
chapter2_2
top N
mこの整数ai（i-1,2,...,m）を大きい順にnこ出力せよ。
制約
m<=10^6
n<=10^3
0 <= ai <= 10^6
input
m
n
a1 a2 a3 ... am
output
b1 b2 b3 ... bn
'''
import copy as cp
def algorithm1(a, n):
    ans = []
    while n > 0:
        m = 0
        for i in a:
            if m < i:
                m = i
        ans.append(m)
        a.remove(m)
        n -= 1
        # n roop
    return ans

def algorithm2(a,n):
    # sort
    a.sort(reverse=True)
    return a[:n]


def algorithm3(a,n,m):
    # array
    arr = [0]*(max(a)+1)
    for i in a:
        arr[i]+=1
    ans = []
    cnt=0
    for i in arr[::-1]:
        if i!=0:
            ans.append(max(a)-cnt)
            n-=1
        cnt+=1
        if n<=0:
            break
    return ans

M = int(input())
N = int(input())
A = list(map(int,input().split()))
print(*algorithm1(cp.deepcopy(A),N))
print(*algorithm2(cp.deepcopy(A),N))
print(*algorithm3(cp.deepcopy(A),N,M))

