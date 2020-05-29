# 양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합
'''
1. 이중 for문 -> 우측 숫자와의 gcd
2. gcd 구하면서 바로 ans에 더함
'''
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)


t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    n = a[0] # 첫번째로 받은 수는 수의 개수 n
    a = a[1:] # 이후의 입력값을 a[1]부터 넣음
    ans = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            ans += gcd(a[i], a[j])
    print(ans)