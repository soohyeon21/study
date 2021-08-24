# 4948

# 어째 작은 입력에 대해서는 밑에 code, 큰 입력은 1st code만 사용하는 것 같다만...
# lambda(), filter()
# 슬슬 소수가 싫어지려 그런다ㅎ

# 다른 사람들 대체적 풀이:
# def function을 만들고, 소수 여부에 따라 True/False return
# 문제에서 준 대로, n의 범위를 정해준다.
# 주어진 범위 내의 수에서만 소수를 찾는다.(ex: 1<= n <=123,456)


import sys
import math

def prime(n):
    ck = [True for x in range(2*n + 1)]
    ck[0] = False
    ck[1] = False
    for i in range(2, (math.ceil(math.sqrt(2*n))) + 1):
        for j in range(i + i, (2*n + 1), i):
            ck[j] = False
    #print(ck) #

    cnt = 0
    for k in range((n + 1), (2*n + 1)):
        if (ck[k] == True):
            cnt += 1
    print(cnt)

while (1):
    n = int(input())

    if (n == 0):
        sys.exit() # while문 안이면 break 써도 되겠다.
    else:
        prime(n)


# 시간 초과
##import sys
##import math
##
##def prime(n):
##    prime = []
##    ans = 0
##    for num in range((n + 1), (2*n + 1)):
##        cnt = 0
##
##        for i in range(1, (math.ceil(math.sqrt(num)) + 1)):
##            if (num % i == 0):
##                cnt += 1
##        if (cnt == 1):
##            #prime.append(num)
##            ans += 1
##
##    #print(prime) #
##    #print(len(prime))
##    print(ans)
##
##while(1):
##    n = int(sys.stdin.readline())
##
##    if (n == 0):
##        sys.exit()
##    elif (n == 1):
##        print(1)
##    else:
##        prime(n)
##    
###print(n)#
