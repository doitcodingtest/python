import sys
input = sys.stdin.readline
N = int(input())
D = [-1]*(N+1)
D[0] = 0
D[1] = 1

def fibo(n):
    if D[n] != -1:  #  기존에 계산한 적이 있는 부분의 문제는 재계산하지 않고 리턴
        return D[n]
    # 메모이제이션: 구한 값을 바로 리턴하지 않고 DP 테이블에 저장한 후 리턴하도록 로직을 구현
    D[n] = fibo(n-2) + fibo(n-1)
    return D[n]

fibo(N)
print(D[N])




