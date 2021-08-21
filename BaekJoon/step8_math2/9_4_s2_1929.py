# 1929

# '에라토스테네스의 체로 풀어 봅시다.'

# 흠... 다른 사람 코드 보니, 비슷하게 for문 (m, n+1), (1, sqrt(num)) 이렇게 두번 돌렸는데,
# def를 이용했을 때는 시간 초과가 안됐네? 왜지?


#
# 맞은 풀이
#
import math

m, n = map(int, input().split())

lt = [0 for x in range(n + 1)]
#print(lt)

for i in range(2, (math.ceil(math.sqrt(n)) + 1)):
    for j in range((i + i), (n + 1), i):
        lt[j] = 1
#print(lt) # 0 == prime
lt[0] = 1
lt[1] = 1

for seq in range(m, (n + 1)):
    if (lt[seq] == 0):
        print(seq)




#
# 0, 1 대신 True, False 사용. 4ms less. 숫자와 bool 별 차이 없는 듯.
#
import math

m, n = map(int, input().split())

lt = [True for x in range(n + 1)]
#print(lt)

for i in range(2, (math.ceil(math.sqrt(n)) + 1)):
    for j in range((i + i), (n + 1), i):
        lt[j] = False
#print(lt) # True = prime
lt[0] = False
lt[1] = False

for seq in range(m, (n + 1)):
    if (lt[seq] == True):
        print(seq)



# 시간 초과1
##import sys
##import math
##
##m, n = map(int, sys.stdin.readline().split())
##
##for num in range(m, (n + 1)):
##    if (num == 1):
##        continue
##    cnt = 0
##    for i in range(2, (math.ceil(math.sqrt(n)) + 1)):
##        if (num % i == 0):
##            cnt += 1
##    if ((num <= math.ceil(math.sqrt(n))) and (cnt == 1)):
##        print(num)
##    elif (cnt == 0):
##        print(num)


# 시간 초과2
##import sys
##import math
##
##m, n = map(int, sys.stdin.readline().split())
##
##for num in range(m, (n + 1)):
##    if (num == 1):
##        continue
##    elif (num == 2):
##        print(num)
##        continue
##    cnt = 0
##    for i in range(1, (math.ceil(math.sqrt(num)) + 1)):
##        if (num % i == 0):
##            cnt += 1
##    if (cnt == 1):
##        print(num)
