N = int(input())
A = [[] for _ in range(N)]
visited = [False] * (N)
D = [0] * (N)
lcm = 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def DFS(v):
    visited[v] = True
    for i in A[v]:
        next = i[0]
        if not visited[next]:
            D[next] = D[v] * i[2] // i[1]
            DFS(next)

for i in range(N - 1):
    a, b, p, q = map(int, input().split())
    A[a].append((b, p, q))
    A[b].append((a, q, p))
    lcm *= (p * q // gcd(p, q))

D[0] = lcm
DFS(0)
mgcd = D[0]
for i in range(1, N):
    mgcd = gcd(mgcd, D[i])
for i in range(N):
    print(int(D[i] // mgcd), end=' ')
