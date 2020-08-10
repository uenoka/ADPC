'''
chapter2_3
ALDS1_1_D Maximum Profit
'''
N = int(input())
R = [int(input()) for i in range(N)]
minr = R[0]
maxr = -10**9
for i in range(1,N):
    maxr = max(maxr, R[i]-minr)
    minr = min(minr,R[i])
print(maxr)
