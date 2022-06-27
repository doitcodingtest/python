import sys
input = sys.stdin.readline

N = int(input())
A = []
for i in range(N):
    A.append((int(input()), i))
Max = 0
sorted_A = sorted(A)
for i in range(N):
    if Max < sorted_A[i][1] - i:    # 정렬 전 index - 정렬 후 index 계산의 최댓값 저장하기
        Max = sorted_A[i][1] - i
print(Max + 1)