import sys
input = sys.stdin.readline
N = int(input());
M = int(input());
A = list(map(int, input().split()))
A.sort()
count = int(0)
i = int(0)
j = int(N-1)
while i < j:    # 투 포인터 이동 원칙 따라 포인터를 이동하며 처리
    if A[i] + A[j] < M:
        i += 1
    elif A[i] + A[j] > M:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1
print(count)