import sys
input = sys.stdin.readline
N = int(input())
D = [0]*(N+2)   # 오늘부터 퇴사일까지 벌 수 있는 최대 수입
T = [0]*(N+1)
P = [0]*(N+1)

for i in range(1, N+1):
    T[i], P[i] = map(int, input().split())

for i in range(N, 0, -1):
    if i+T[i] > N+1:
        D[i] = D[i+1]
    else:
        D[i] = max(D[i+1], P[i] + D[i+T[i]])

print(D[1])