'''
TSP 문제
n개의 도시 모두 거쳐 다시 원래 도시로 올 때 최소비용
'''
def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    j = len(a)-1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True


n = int(input()) # 도시의 수
w = [list(map(int, input().split())) for _ in range(n)] # n개의 w
# w[0][[첫번째 input], w[1][두번째 input], ...
d = list(range(n)) # range(n) -> 0부터 n-1까지
# d[0, 1, ..., n-1]
ans = 9999999999 # 최솟값을 구하기위해 초깃값을 크게 넣어둠
while True:
    ok = True
    s = 0
    for i in range(0, n-1): # 0부터 n-2까지
        if w[d[i]][d[i+1]] == 0:
            ok = False
            break
        else:
            s += w[d[i]][d[i+1]]
    if ok and w[d[-1]][d[0]] != 0:
        s += w[d[-1]][d[0]]
        ans = min(ans, s)
    if not next_permutation(d):
        break
print(ans)