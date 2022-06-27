import sys
input = sys.stdin.readline
N, M = map(int, input().split())  # 수의 개수, 변경이 일어나는 횟수, 구간 합을 구하는 횟수
treeHeight = 0
lenght = N

while lenght != 0:
    lenght //= 2
    treeHeight += 1

treeSize = pow(2, treeHeight + 1)
leftNodeStartIndex = treeSize // 2 - 1
tree = [sys.maxsize] * (treeSize + 1)

# 데이터를 리프노드에 저장
for i in range(leftNodeStartIndex + 1, leftNodeStartIndex + N + 1):
    tree[i] = int(input())


# 인덱스 트리 생성 함수
def setTree(i):
    while i != 1:
        if tree[i // 2] > tree[i]:
            tree[i // 2] = tree[i]
        i -= 1

setTree(treeSize - 1)

# 최소값 계산 함수
def getMin(s, e):
    Min = sys.maxsize
    while s <= e:
        if s % 2 == 1:
            Min = min(Min, tree[s])
            s += 1
        if e % 2 == 0:
            Min = min(Min, tree[e])
            e -= 1
        s = s // 2
        e = e // 2
    return Min

for _ in range(M):
    s, e = map(int, input().split())
    s = s + leftNodeStartIndex
    e = e + leftNodeStartIndex
    print(getMin(s, e))
