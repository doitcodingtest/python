import sys
input = sys.stdin.readline
N = int(input())
W = []
for i in range(N):
 W.append([])
 W[i] = list(map(int, input().split()))
D = [[0 for j in range(1 << 16)] for i in range(16)]

def tsp(c,v):
    if v == (1<<N)-1:
        if W[c][0] == 0:
            return float('inf')
        else:
            return W[c][0]
    if D[c][v] != 0:
        return D[c][v]
    min_val = float('inf')
    for i in range(0, N):
        if (v & (1<<i)) == 0 and W[c][i] != 0:
            min_val = min(min_val, tsp(i, (v | (1 << i))) + W[c][i])
    D[c][v] = min_val
    return D[c][v]

print(tsp(0,1))
