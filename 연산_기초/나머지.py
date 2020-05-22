# (A+B)%C, ((A%C) + (B%C))%C, (A×B)%C, ((A%C) × (B%C))%C 출력
a, b, c = map(int,input().split())
print((a + b) % c)
print(((a%c) + (b%c)) % c)
print((a*b) % c)
print(((a%c) * (b%c)) % c)