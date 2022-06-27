import sys
N, M = map(int, input().split())
distance = [[sys.maxsize for j in range(N+1)] for i in range(N+1)]
for i in range(1, N+1): # 인접 행렬 초기화
    distance[i][i] = 0

for i in range(M):
    s, e = map(int, input().split())
    distance[s][e] = 1
    distance[e][s] = 1

# 플로이드 워셜 수행
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

Min = sys.maxsize
Answer = -1
for i in range(1, N+1):
    temp = 0
    for j in range(1, N+1):
        temp += distance[i][j]
    if Min > temp:  # 가장 작은 케빈 베이컨의 수를 지닌 i 찾기
        Min = temp
        Answer = i

print(Answer)
