# 1978

# 소수의 정의를 이용한 풀이. 약수로 1과 자기 자신만 갖는 수.
# or
# 에라토스테네스의 체. 전체에서 제하기. sqrt(전체) 수의 배수까지만 하면 됨.

# continue는 곧바로 건너뛰기.
# pass는 그냥 빈 명령줄.


# 맞은 풀이1
n = int(input())
a = list(map(int, input().split()))

fin = 0
np = [2, 3, 5, 7]
for i in a:
    if (i == 1):
        pass
    elif (i in np):
        fin += 1
    else: # 찾기 시작
        num = 2
        cnt = 0
        while (num < (i + 1)):
            if (i % num == 0):
                cnt += 1
            num += 1
        if (cnt == 1):
            fin += 1
print(fin)


# 맞은 풀이2
n = int(input())
a = list(map(int, input().split()))

fin = 0
for i in a:
    if (i == 1): # 1 is not prime
        continue # continue: 아예 건너 뜀. # pass: if문까지는 돌아감.
    else: # 찾기 시작 # continue이므로 굳이 else 아니어도 될 듯.
        cnt = 0
        for j in range(2, (i + 1)): # while문 안써도 됨.
            if (i % j == 0):
                cnt += 1
        if (cnt == 1):
            fin += 1
print(fin)


# 틀린 풀이
##n = int(input())
##a = list(map(int, input().split()))
##
##pn = [2, 3, 5, 7, 11]
##fin = 0
##for i in a:
##    for j in pn:
##        if ((i < 12) and (i in pn)): # prime
##            #fin += 1
##            pass
##        elif ((i == 1) or (i % j == 0)): # not prime
##            pass
##        else: # 5개의 배수는 아님
##            pn.append(i)
##for k in range(len(pn)):
##    if (pn[k]**2 in pn):
##        pn[pn.index(pn[k]**2)] = 0
##        print(pn)
##for number in a:
##    if (number in pn):
##        fin += 1
##        print(number)
##    print(a)
##print(fin)


#import math   
#sqrt = math.floor(math.sqrt(1000))
