# 2775

# index는 0, 1, 2, 3, ..., (n-1) 이렇게 해서 n개.
# a = [x for x in range(1, n)] ==> a = [1, 2, 3, 4, ..., (n-1)]

t = int(input())

for i in range(t):
    k = int(input()) # k층
    n = int(input()) # n호
    people = [x for x in range(1, (n + 1))] # 0층
    for kk in range(1, (k + 1)):
        for a in range(1, n):
            people[a] = people[a - 1] + people[a] # 1~k층. 최종 k층
    print(people[n - 1])
    

# 시간초과.... using 재귀
##def th(a, b): # a층 b호
##    if (a == 0):
##        return b
##    else:
##        n = 0
##        for i in range(1, (b + 1)):
##            n += th((a - 1), i)
##        return n
##
##t = int(input())
##
##for i in range(t): # k층 n호
##    k = int(input())
##    n = int(input())
##    print(th(k, n))

# 연습하던 코드. wrong code
##def th(a, b): # a층 b호
##    com = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
##    if ((a in com) and ((b - a) < -2)):
##        return th()
##    if (a == 0):
##        return b
##    else:
##        n = 0
##        for i in range(1, (b + 1)):
##            n += th((a - 1), i)
##        return n
##
##t = int(input())
##
##for i in range(t): # k층 n호
##    k = int(input())
##    n = int(input())
##    print(th(k, n))




