N = int(input())
K = int(input())
start = 1
end = K
ans = 0
# 이진 탐색 수행
while start <= end:
    middle = int((start + end) / 2)
    cnt = 0
    # 중앙 값보다 작은 수 계산
    for i in range(1, N + 1):
        cnt += min(int(middle / i), N)  # 작은 수 카운트 핵심 로직
    if cnt < K:
        start = middle + 1
    else:
        ans = middle
        end = middle - 1
print(ans)
