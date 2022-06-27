from collections import deque

N, M, Start = map(int, input().split())
A = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)  # 양방향 에지이므로 양쪽에 에지를 더하기
    A[e].append(s)
for i in range(N + 1):
    A[i].sort()  # 번호가 작은 노드 부터 방문하기 위해 정렬하기
visited = [False] * (N + 1)


def DFS(v):
    print(v, end=' ')
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)


DFS(Start)

visited = [False] * (N + 1)  # 리스트 초기화


def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        print(now_Node, end=' ')
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


print()
BFS(Start)
