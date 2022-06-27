import copy
import sys
from collections import deque
from queue import PriorityQueue
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())
myMap = [[0 for j in range(M)] for i in range(N)]
visited = [[False for j in range(M)] for i in range(N)]

for i in range(N):
    myMap[i] = list(map(int, input().split()))

sNum = 1
sumlist = list([])
mlist = []

def addNode(i, j, queue):
    myMap[i][j] = sNum
    visited[i][j] = True
    temp = [i, j]
    mlist.append(temp)
    queue.append(temp)

def BFS(i, j):
    queue = deque()
    mlist.clear()
    start = [i, j]
    queue.append(start)
    mlist.append(start)
    visited[i][j] = True
    myMap[i][j] = sNum
    while queue:
        r, c = queue.popleft()
        for d in range(4):
            tempR = dr[d]
            tempC = dc[d]
            while r + tempR >= 0 and r + tempR < N and c + tempC >= 0 and c + tempC < M:
                if not visited[r + tempR][c + tempC] and myMap[r + tempR][c + tempC] != 0:
                    addNode(r + tempR, c + tempC, queue);
                else:
                    break;
                if tempR < 0:
                    tempR -= 1
                elif tempR > 0:
                    tempR += 1
                elif tempC < 0:
                    tempC -= 1
                elif tempC > 0:
                    tempC += 1
    return mlist

for i in range(N):
    for j in range(M):
        if myMap[i][j] != 0 and not visited[i][j]:
            tempList = copy.deepcopy(BFS(i, j))  # 깊은 복사로 해주어야 주소를 공유하지 않음
            sNum += 1
            sumlist.append(tempList)

pq = PriorityQueue()
for now in sumlist:
    for temp in now:
        r = temp[0]
        c = temp[1]
        now_S = myMap[r][c]
        for d in range(4):
            tempR = dr[d]
            tempC = dc[d]
            blenght = 0
            while r + tempR >= 0 and r + tempR < N and c + tempC >= 0 and c + tempC < M:
                if myMap[r + tempR][c + tempC] == now_S:  # 같은 섬이면 에지를 만들 수 없음
                    break
                elif myMap[r + tempR][c + tempC] != 0:  # 같은 섬도 아니고 바다도 아니면
                    if blenght > 1:  # 다른 섬 → 길이가 1 이상일 때 에지로 더하기
                        pq.put((blenght, now_S, myMap[r + tempR][c + tempC]))
                    break
                else:  # 바다이면 다리의 길이 연장
                    blenght += 1
                if tempR < 0:
                    tempR -= 1
                elif tempR > 0:
                    tempR += 1
                elif tempC < 0:
                    tempC -= 1
                elif tempC > 0:
                    tempC += 1


def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


parent = [0] * sNum
for i in range(len(parent)):
    parent[i] = i

useEdge = 0
result = 0
while pq.qsize() > 0:
    v, s, e = pq.get()
    if find(s) != find(e):
        union(s, e)
        result += v
        useEdge += 1

if useEdge == sNum - 2:
    print(result)
else:
    print(-1)
