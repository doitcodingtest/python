import sys
input = sys.stdin.readline
mod = 1000000007
N, L, R = map(int, input().split())
D = [[[0 for k in range(101)] for j in range(101)] for i in range(101)]
D[1][1][1] = 1  # 빌딩이 1개이면 놓을 수 있는 경우의 수는 1개

for i in range(2, N + 1):
    for j in range(1, L + 1):
        for k in range(1, R + 1):
            D[i][j][k] = (D[i-1][j][k] * (i-2) + (D[i-1][j][k-1] + D[i-1][j-1][k])) % mod

print(D[N][L][R])