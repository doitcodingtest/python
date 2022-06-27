import sys
sys.setrecursionlimit(10 ** 6)  # 재귀 함수를 위해 충분히 큰수로 한계 값 설정

input = sys.stdin.readline
N = int(input())
visited = [False] * (N)
tree = [[] for _ in range(N)]
answer = 0
p = list(map(int, input().split()))
for i in range(N):
    if p[i] != -1:
        tree[i].append(p[i])
        tree[p[i]].append(i)
    else:
        root = i


# DFS 탐색 함수
def DFS(number):
    global answer
    visited[number] = True
    cNode = 0
    for i in tree[number]:
        if not visited[i] and i != deleteNode:  # 삭제 노드가 아닐 때도 탐색 중지
            cNode += 1
            DFS(i)
    if cNode == 0:
        answer += 1  # 자식 노드가 0개이면 리프노드이므로 정답 값 층가


deleteNode = int(input())
if deleteNode == root:
    print(0)
else:
    DFS(root)
    print(answer)
