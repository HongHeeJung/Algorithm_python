import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d = [[0]*n for _ in range(n)]
for i in range(n):
    d[i][i] = True
for i in range(n-1):
    if a[i] == a[i+1]:
        d[i][i+1] = True
for k in range(3, n+1):
    for i in range(0, n-k+1):
        j = i+k-1
        if a[i] == a[j] and d[i+1][j-1]:
            d[i][j] = True
m = int(sys.stdin.readline().split())
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(1 if d[s-1][e-1] else 0)