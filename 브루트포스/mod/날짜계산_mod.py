'''
지구 E<=15 태양 S<=28 달 M<19
15년 = 15 15 15
16년 = 1 16 16
20년 = 5 20 1

mod 이용
'''
e, s, m = map(int, input().split())
e -= 1
s -= 1
m -= 1
year = 0
while True:
    if year % 15 == e and year % 28 == s and year % 19 == m:
        print(year + 1)
        break
    year += 1