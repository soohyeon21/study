# 3460

# bin() # 10->2진수
    # '0b11' 이런 식으로 return하므로, bin(3)[2:]를 사용.
# abs() # 절댓값 구하는 내장함수
# enumerate() # indes와 element return
    # for i, v in enumerate(리스트/문자열): #이런 식으로 사용.

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    bbin = ""
    num = 0
    n = int(sys.stdin.readline())
    binary = bin(n)[2:]
##    print(binary)
    for letter in binary:
        bbin = letter + bbin
##    print(bbin)
    for i in range(len(bbin)):
        if (bbin[i] == "1"):
            print(i, end=" ")

#
# 틀린 풀이
#
# 여러 예시를 돌려보았으나, 이 아이는 왜 틀린 것인지 모르겠다.
# 심지어 얘는 마지막 요소 뒤에 공백도 없다고!!!!!!!
#
##import sys
##
##t = int(sys.stdin.readline())
##
##for _ in range(t):
##    bbin = ""
##    num = 0
##    n = int(sys.stdin.readline())
##    binary = bin(n)[2:]
####    print(binary)
##    for letter in binary:
##        bbin = letter + bbin
####    print(bbin) 
##    for i in range(len(bbin)):
##        if (bbin[i] == "1"):
##            if (num == 0):
##                print(str(i), end="")
##                num += 1
##            else:
##                print(" " + str(i), end="")
