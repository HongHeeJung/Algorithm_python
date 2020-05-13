n = int(input())
m = int(input())
no = [False] * 10
if m > 0:
    a = list(map(int, input().split()))
else:
    a = []
for x in a:
    no[x] = True


def go(c):
    if c == 0:
        if no[0]:
            return 0
        else:
            return 1
    l = 0
    while c > 0:
        if no[c%10]:
            return 0
        l += 1
        c //=10
    return l


ans = abs(n-100)
for i in range(0, 1000000+1):
    c = i
    l = go(c)
    if l > 0:
        press = abs(c-n)
        if ans > l + press:
            ans = l + press
print(ans)