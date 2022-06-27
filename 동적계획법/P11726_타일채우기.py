mod = 10007
N = int(input())
D = [0]*1001
D[1] = 1  # 길이가 2 × 1일 때 타일의 경우의 수
D[2] = 2  # 길이가 2 × 2일 때 타일의 경우의 수

for i in range(3, N+1):
    D[i] = (D[i-1]+D[i-2]) % mod
print(D[N])

