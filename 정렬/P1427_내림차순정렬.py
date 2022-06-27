import sys
print = sys.stdout.write
A = list(input())
for i in range(len(A)):
    Max = i
    for j in range(i+1, len(A)):
        if A[j] > A[Max]:   # 내림차순이므로 최댓값을 찾음
            Max = j
    if A[i] < A[Max]:
        temp = A[i]
        A[i] = A[Max]
        A[Max] = temp
for i in range(len(A)):
    print(A[i])