import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N, M = map(int, input().split())
arrive = False
A = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)


def DFS(now, depth):
    global arrive
    if depth == 5 or arrive == True:    # 깊이가 5가 되면 종료
        arrive = True
        return
    visited[now] = True
    for i in A[now]:
        if not visited[i]:
            DFS(i, depth + 1)   # 재귀 호출 마다 깊이 증가
    visited[now] = False


for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)  # 양방향 에지이므로 양쪽에 에지를 더하기
    A[e].append(s)

for i in range(N):
    DFS(i, 1)
    if arrive:
        break
if arrive:
    print(1)
else:
    print(0)
