import sys
input = sys.stdin.readline
N = int(input())
tree = {}  # 딕셔너리 형태로 선언
for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

def preOrder(now):
    if now == '.':
        return
    print(now, end='')  # 1.현재 노드
    preOrder(tree[now][0])  # 2.왼쪽 탐색
    preOrder(tree[now][1])  # 3.오른쪽 탐색

def inOrder(now):
    if now == '.':
        return
    inOrder(tree[now][0])  # 1.왼쪽 탐색
    print(now, end='')  # 2.현재 노드
    inOrder(tree[now][1])  # 3.오른쪽 탐색

def postOrder(now):
    if now == '.':
        return
    postOrder(tree[now][0])  # 1.왼쪽 탐색
    postOrder(tree[now][1])  # 2.오른쪽 탐색
    print(now, end='')  # 3.현재 노드

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
