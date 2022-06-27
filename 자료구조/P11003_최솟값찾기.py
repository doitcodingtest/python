from collections import deque
N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))
for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    mydeque.append((now[i],i))
    if mydeque[0][1] <= i - L: # 범위에서 벗어난 값은 덱에서 제거
        mydeque.popleft()
    print(mydeque[0][0], end=' ')




