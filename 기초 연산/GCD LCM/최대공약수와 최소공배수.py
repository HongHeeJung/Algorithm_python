# 유클리드 호재법 gcd(a,b) = gcd(b,r) if r==0, 그때 b가 최대 공약수
def gcd(x, y):
    if y == 0:
        return x
    else:
        # print(x%y)
        return gcd(y, x%y)


a, b = map(int, input().split())
g = gcd(a, b)
print(g)
print(a*b//g)