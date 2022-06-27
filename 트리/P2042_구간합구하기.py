import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())  # 수의 개수, 변경이 일어나는 횟수, 구간 합을 구하는 횟수
treeHeight = 0
lenght = N

while lenght != 0:
    lenght //= 2
    treeHeight += 1

treeSize = pow(2, treeHeight + 1)
leftNodeStartIndex = treeSize // 2 - 1
tree = [0] * (treeSize + 1)

# 데이터를 리프노드에 저장
for i in range(leftNodeStartIndex + 1, leftNodeStartIndex + N + 1):
    tree[i] = int(input())

# 인덱스 트리 생성 함수
def setTree(i):
    while i != 1:
        tree[i // 2] += tree[i]
        i -= 1

setTree(treeSize - 1)


# 값 변경 함수
def changeVal(index, value):
    diff = value - tree[index]
    while index > 0:
        tree[index] = tree[index] + diff
        index = index // 2

# 구간 합 계산 함수
def getSum(s, e):
    partSum = 0
    while s <= e:
        if s % 2 == 1:
            partSum += tree[s]
            s += 1
        if e % 2 == 0:
            partSum += tree[e]
            e -= 1
        s = s // 2
        e = e // 2
    return partSum

for _ in range(M + K):
    question, s, e = map(int, input().split())
    if question == 1:
        changeVal(leftNodeStartIndex + s, e)
    elif question == 2:
        s = s + leftNodeStartIndex
        e = e + leftNodeStartIndex
        print(getSum(s, e))
