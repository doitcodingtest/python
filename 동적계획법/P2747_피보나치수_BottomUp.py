import sys
input = sys.stdin.readline
N = int(input())
D = [-1]*(N+1)
D[0] = 0
D[1] = 1

for i in range(2, N+1):
    D[i] = D[i-2] + D[i-1]

print(D[N])
