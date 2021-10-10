# 10214

t = int(input())
Y, K = 0, 0

for _ in range(t):
    for i in range(9):
        y, k = map(int, input().split())
        Y += y
        K += k
    if (Y > K):
        print("Yonsei")
    elif (Y < K):
        print("Korea")
    else:
        print("Draw")
