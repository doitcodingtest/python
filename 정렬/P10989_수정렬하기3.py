import sys
input = sys.stdin.readline
N = int(input())
count = [0] * 10001
for i in range(N):
    count[int(input())] += 1
for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)
