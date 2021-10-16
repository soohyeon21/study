# 2444

n = int(input())

a = n - 1
b = 1
for i in range(2*n - 1):
    print(" "*a + "*"*b)
    if (i <= (n - 2)):
        a -= 1
        b += 2
    else:
        a += 1
        b -= 2
