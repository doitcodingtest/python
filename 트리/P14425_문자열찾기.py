import sys
input = sys.stdin.readline
n, m = map(int, input().split())
textList = set([input() for _ in range(n)])
count = 0
for _ in range(m):
    subText = input()
    if subText in textList:
        count += 1
print(count)