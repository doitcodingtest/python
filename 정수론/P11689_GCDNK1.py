import math
N = int(input())
result = N
for p in range(2, int(math.sqrt(N)) + 1):  # 제곱근까지만 진행
    if N % p == 0:  # p가 소인수인지 확인
        result -= result / p  # 결괏값 업데이트
        while N % p == 0:  # 2의 7승*11이라면 2의 7승을 없애고 11만 남김
            N /= p
if N > 1:  # 반복문에서 제곱근까지만 탐색했으므로 1개의 소인수가 누락되는 케이스 처리
    result -= result / N
print(int(result))
