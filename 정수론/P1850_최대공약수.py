def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a, b = map(int, input().split())
result = gcd(a, b)
while result > 0:
    print(1, end='')
    result -= 1
