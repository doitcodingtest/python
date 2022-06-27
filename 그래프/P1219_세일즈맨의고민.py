import sys
input = sys.stdin.readline
N, sCity, eCity, M = map(int, input().split())
edges= []
distance = [-sys.maxsize] * N  # 최단거리 배열 초기화

for _ in range(M):
    start, end, price = map(int, input().split())
    edges.append((start, end, price))

cityMoney = list(map(int, input().split()))

# 변형된 벨만포드 수행
distance[sCity] = cityMoney[sCity]  # 출발 초기화
# 양수 사이클이 전파 되도록 충분히 큰 수로 반복
for i in range(N+101):
    for start, end, price in edges:
        if distance[start] == -sys.maxsize:
            continue
        elif distance[start] == sys.maxsize:
            distance[end] = sys.maxsize
        elif distance[end] < distance[start] + cityMoney[end] - price:
            distance[end] = distance[start] + cityMoney[end] - price
            if i >= N-1:
                distance[end] = sys.maxsize

if distance[eCity] == -sys.maxsize:
    print("gg")
elif distance[eCity] == sys.maxsize:
    print("Gee")
else:
    print(distance[eCity])

