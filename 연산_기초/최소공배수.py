def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)


t = int(input()) # 테스트케이스
for _ in range(t):
    a, b = map(int, input().split())
    g = gcd(a, b)
    print(a*b//g)