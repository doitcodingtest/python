import sys
input = sys.stdin.readline
N = int(input())
D = [[0 for j in range(2)] for i in range(N+1)]
D[1][1] = 1 # 1자리 이친수는 1 한 가지만 있음
D[1][0] = 0

for i in range(2, N+1):
    D[i][0] = D[i-1][1] + D[i-1][0]
    D[i][1] = D[i-1][0]

print(D[N][0] + D[N][1])