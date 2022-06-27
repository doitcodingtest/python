N = int(input())
distance = [[0 for j in range(N)] for i in range(N)]

# 인접 행렬 데이터 저장
for i in range(N):
    distance[i] = list(map(int, input().split()))

# 변형된 플로이드 워셜 수행
for k in range(N):
    for i in range(N):
        for j in range(N):
            if distance[i][k] == 1 and distance[k][j] == 1:
                distance[i][j] = 1

for i in range(N):
    for j in range(N):
        print(distance[i][j], end=' ')
    print()
