# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력
def find(x):
    if x < 2:
        return False
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

n = int(input())
a = list(map(int, input().split()))
ans = 0
for x in a:
    if find(x):
        ans += 1
print(ans)