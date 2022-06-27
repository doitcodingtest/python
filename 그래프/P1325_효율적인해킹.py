import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
A = [[] for _ in range(N + 1)]
answer = [0] * (N + 1)


def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                answer[i] += 1  # 신규 노드 인덱스의 정답 리스트 값을 증가
                queue.append(i)


for _ in range(M):
    S, E = map(int, input().split())
    A[S].append(E)

for i in range(1, N + 1):  # 모든 노드에서 BFS 실행
    visited = [False] * (N + 1)
    BFS(i)

maxVal = 0
for i in range(1, N + 1):
    maxVal = max(maxVal, answer[i])

for i in range(1, N + 1):
    if maxVal == answer[i]:
        print(i, end=' ')
