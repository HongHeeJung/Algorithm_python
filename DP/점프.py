n = int(input()) # n 받기
a = [list(map(int, input().split())) for _ in range(n)] # 이동가능 칸 수 받기
d = [[0]*n for _ in range(n)] # 이동 경로 개수 저장
d[0][0] = 1 # 처음은 1
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        for k in range(j):
            if k + a[i][k] == j: # k에서 a[i][k]만큼 더한게 j이면 거기로 이동
                d[i][j] += d[i][k] # 거기로 갈 수 있는 경우를 이전까지 갈 수 있는 경우만큼 더함
        for k in range(i):
            if k + a[k][j] == i:
                d[i][j] += d[k][j]
print(d[n-1][n-1]) # 마지막 출력