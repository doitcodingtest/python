import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)

index = 0
maxLength = 1
B = [0] * 1000001
D = [0] * 1000001
ans = [0] * 1000001
B[maxLength] = A[1]
D[1] = 1

# 바이너리 서치 구현
def binarysearch(l, r, now):
    while l < r:
        mid = (l + r) // 2
        if B[mid] < now:
            l = mid + 1
        else:
            r = mid
    return l

for i in range(2, N + 1):
    if B[maxLength] < A[i]:  # 가장 마지막 수열보다 현재 수열이 큰 경우
        maxLength += 1
        B[maxLength] = A[i]
        D[i] = maxLength
    else:  # 바이너리 서치를 이용해 현재 수열이 들어갈 index 찾기
        index = binarysearch(1, maxLength, A[i])
        B[index] = A[i]
        D[i] = index

print(maxLength)
index = maxLength
x = B[maxLength] + 1
for i in range(N, 0, -1):
    if D[i] == index and A[i] < x:
        ans[index] = A[i]
        x = A[i]
        index -= 1

for i in range(1, maxLength + 1):
    print(ans[i], end=' ')
