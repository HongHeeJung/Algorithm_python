'''
N개의 정수로 이루어진 배열 A
정수 순서 바꿔서
|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]| 식의 최댓값
'''
# 식 계산
def calc(a):
    ans = 0 # 식 결과
    for i in range(1, len(a)):
        ans += abs(a[i]-a[i-1])
    return ans


# 다음 순열 구하는 함수
def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a) - 1
    while a[j] <= a[i-1]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True


n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
while True:
    temp = calc(a)
    ans = max(ans, temp)
    if not next_permutation(a):
        break
print(ans)