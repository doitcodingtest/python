import sys
input = sys.stdin.readline
N, K = map(int, input().split())
D = [[0 for j in range(N+1)] for i in range(N+1)]

for i in range(0, N+1):
    D[i][1] = i
    D[i][0] = 1
    D[i][i] = 1

for i in range(2, N+1):
    for j in range(1, i):
        D[i][j] = D[i-1][j] + D[i-1][j-1]
        D[i][j] = D[i][j] % 10007

print(D[N][K])