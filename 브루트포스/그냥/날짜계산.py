'''
지구 E<=15 태양 S<=28 달 M<19
15년 = 15 15 15
16년 = 1 16 16
20년 = 5 20 1

mod 이용
구하고자 하는 year까지 하나씩 올리며 구함
'''
E, S, M = map(int,input().split())
e, s, m = 1, 1, 1 # 매개값 (초기값은 1)
year = 1 # 구하고자 하는 연도
while True:
    # 주어진 E, S, M이 되었을 때의 year를 출력
    if e == E and s == S and m == M:
        print(year)
        break
    e += 1
    s += 1
    m += 1
    # 매개변수가 기준값을 넘으면 1로 초기화
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1
    year += 1