import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
A = list(input())
A.pop()  # \n 문자열 제거
B = list(input())
B.pop()  # \n 문자열 제거
DP = [[0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]
Path = []
for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            DP[i][j] = DP[i - 1][j - 1] + 1  # 같은 문자열일 때 왼쪽 대각선 값 + 1
        else:
            DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])  # 다르면 왼쪽과 위의 값 중 큰 수

print(DP[len(A)][len(B)])


# LCS 구현 함수
def getText(r, c):
    if r == 0 or c == 0:
        return
    if A[r - 1] == B[c - 1]:  # 같으면 LCS에 기록하고 왼쪽위로 이동
        Path.append(A[r - 1])
        getText(r - 1, c - 1)
    else:  # 다르면 왼쪽과 중 큰 수로 이동
        if DP[r - 1][c] > DP[r][c - 1]:
            getText(r - 1, c)
        else:
            getText(r, c - 1)


getText(len(A), len(B))

for i in range(len(Path) - 1, -1, -1):
    print(Path.pop(i), end='')
print()
