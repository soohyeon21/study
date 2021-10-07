# 9506

# end=''를 사용해서 다음 print문에서 이어서 출력하는 방법도 있다.

while (True):
    n = int(input())
    if (n == -1):
        break
    
    factor = [1]
    for fac in range(2, n // 2 + 1):
        if (n % fac == 0):
            factor.append(fac)

    perfect = ''
    if (n == sum(factor)):
        perfect += str(n)
        perfect += " = 1"
        for i in range(1, len(factor)):
            perfect += (" + " + str(factor[i]))
        print(perfect)
    else:
        print("{} is NOT perfect." .format(n))
