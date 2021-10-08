# 10162

# 뭔가 느낌이 greedy algorithm인걸?

# a = 300초, b = 60초, c = 10초
t = int(input())
a = 300
b = 60
c = 10
A, B, C = 0, 0, 0

if (t % 10 != 0):
    print(-1)
else:
    A += t // a
    t %= a
    B += t // b
    t %= b
    C += t // c
    t %= c
    print(A, B, C)
