import sys
input = sys.stdin.readline
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
    queue = [node]
    visited[node] = True
    while queue:
        now_node = queue.pop(0)
        for next in tree[now_node]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                parent[next] = now_node # 부모 노드 저장
                depth[next] = depth[now_node]+1 # 노드 depth 저장
       
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
mydict = dict()
for _ in range(M):
    a, b = map(int, input().split())
    if not mydict.get((a, b), 0): #같은 질문일 경우 재계산을 하지 않기 위해 딕셔너리 자료형 사용
        mydict[(a, b)] = mydict[(b, a)] = excuteLCA(a, b)
    print(mydict.get((a, b)))
