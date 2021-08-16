# 2839

# 우선순위는 5kg이다.
# 5로 나눈 것의 나머지에 따라 과정을 달리하자.
# 다른 사람들을 대부분 그냥 5로 나누고, 계속 -3을 하는 코드를 작성한 듯 하다.

####################################################

# first try code

n = int(input())

quo5 = n // 5
quo3 = 0
rem5 = n % 5

if (rem5 == 0):
    print(quo5)
elif (rem5 == 1):
    if (quo5 >= 1):
        quo5 -= 1
        quo3 += 2
        print(quo5 + quo3)
    else:
        print(-1)
elif (rem5 == 2):
    if (quo5 >= 2):
        quo5 -= 2
        quo3 += 4
        print(quo5 + quo3)
    else:
        print(-1)
elif (rem5 == 3):
    quo3 += 1
    print(quo5 + quo3)
elif (rem5 == 4):
    if (quo5 >= 1):
        quo5 -= 1
        quo3 += 3
        print(quo5 + quo3)
    else:
        print(-1)
else:
    print(-1)

######################################################

# else 한꺼번에 처리 ver.

n = int(input())

quo5 = n // 5
quo3 = 0
rem5 = n % 5

if (rem5 == 0):
    print(quo5 + quo3)
elif ((rem5 == 1) and (quo5 >= 1)):
    quo5 -= 1
    quo3 += 2
    print(quo5 + quo3)
elif ((rem5 == 2) and (quo5 >= 2)):
    quo5 -= 2
    quo3 += 4
    print(quo5 + quo3)
elif (rem5 == 3):
    quo3 += 1
    print(quo5 + quo3)
elif ((rem5 == 4) and (quo5 >= 1)):
    quo5 -= 1
    quo3 += 3
    print(quo5 + quo3)
else:
    print(-1)

######################################################

# shortest code ver.

n = int(input())

bag = n // 5
rem5 = n % 5

if (rem5 == 0):
    pass
elif ((rem5 == 1) and (bag >= 1)):
    bag += 1
elif ((rem5 == 2) and (bag >= 2)):
    bag += 2
elif (rem5 == 3):
    bag += 1
elif ((rem5 == 4) and (bag >= 1)):
    bag += 2
else:
    bag = -1
    
print(bag)







