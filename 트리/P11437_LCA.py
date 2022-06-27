import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(0, N-1): # 인접 리스트에 트리 데이터 저장
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

depth = [0]*(N+1)
parent = [0]*(N+1)
visited = [False]*(N+1)

def BFS(node):
    queue = deque()
    queue.append(node)
    visited[node] = True
    level = 1
    now_size = 1
    count = 0
    while queue:
        now_node = queue.popleft()
        for next in tree[now_node]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                parent[next] = now_node # 부모 노드 저장
                depth[next] = level # 노드 depth 저장
        count += 1
        if count == now_size:
            count = 0
            now_size = len(queue)
            level += 1

BFS(1)

def excuteLCA(a, b):
    if depth[a] < depth[b]:
        temp = a
        a = b
        b = temp

    while depth[a] != depth[b]:
        a = parent[a]

    while a != b:
        a = parent[a]
        b = parent[b]

    return a

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(str(excuteLCA(a,b)))
    print("\n")



