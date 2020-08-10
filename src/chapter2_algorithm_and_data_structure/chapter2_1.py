'''
chapter2_1
Top 3
10人のプレイヤーの得点上位3つを出力する
sample
input
1 2 4 2 6 6 12 34 32 21
output
34 32 21
'''
A = list(map(int,input().split()))
A.sort(reverse=True)
print(*A[:3])