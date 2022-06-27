import sys
input = sys.stdin.readline
N = int(input())
W = []
for i in range(N):
    W.append([])
    W[i] = list(map(int, input().split()))

D = [[0 for j in range(1 << 16)] for i in range(16)]
for i in range(N):
    for j in range(0, 1 << N):
        D[i][j] = sys.maxsize


def tsp(c, v):
    if v == (1 << N) - 1:
        if W[c][0] == 0:
            return sys.maxsize
        else:
            return W[c][0]
    if D[c][v] != sys.maxsize:
        return D[c][v]
    for i in range(0, N):
        if (v & (1 << i)) == 0 and W[c][i] != 0:
            D[c][v] = min(D[c][v], tsp(i, (v | (1 << i))) + W[c][i])
    return D[c][v]


print(tsp(0, 1))
