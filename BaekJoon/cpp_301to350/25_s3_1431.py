# 1431

# 특정 기준에 따라 정렬할 수 있는 거라면 sort-key-lambda를 적극 고려하자.
# 이미 사람들이 다 만들어 놓은 기능을 적극 활용하자.

# .sort(key=lambda x:(len(x), sum(int(a) for a in x if a.isnumeric()), x))
# isnumeric()
# isdigit()
# 단, '.'을 포함해서 문자가 하나라도 포함되어 있으면 안됨.


#
# solution
#
import sys

n = int(sys.stdin.readline())
serial = [sys.stdin.readline().rstrip() for x in range(n)]
sumNnum = []

for num in serial:
    digit = 0
    for letter in num:
        if ((48 <= ord(letter)) and (ord(letter) <= 57)):
            digit += int(letter)
    sumNnum.append((digit, num))

sumNnum.sort(key=lambda x:(len(x[1]), x[0], x[1]))

for i in range(n):
    print(sumNnum[i][1])


#
# 막 고민하다가 중간에 더 좋은 방법이 떠오르기 전까지 작성하던 코드
#
##import sys
##
##n = int(sys.stdin.readline())
##serial = [sys.stdin.readline().rstrip() for _ in range(n)]
##
### 1. 짧은 것 먼저
##serial.sort(key=lambda x: len(x))
##
### 2. 길이 같을 때, 작은 합 먼저
##clen = len(serial[0])
##comp = []
##serial.append("")
##for i in range(n+1):
##    if (len(serial[i]) == clen):
##        comp.append(serial[i])
##        continue
##    elif (len(comp) == 1):
##        pass
##    else:
##        # 처리하고
##        print("comp", comp)
##        same = {}
##        chk_digit = []
##        put_val = []
##        for val in comp:
##            digit = 0
##            for letter in val:
##                if ((48 <= ord(letter)) and (ord(letter) <= 57)):
##                    digit += int(letter)
##            chk_digit.append(digit)
##            if (digit in chk_digit):
##                put_val.append((digit, val))
##            else:
##                same[digit] = val
##        same_keys = list(same.keys())
##        same_keys.sort()
##        print("same_keys", same_keys)
##        same_list = [same[same_keys[x]] for x in range(len(same_keys))]
##        # 3. 사전순
##        if (len(comp) != len(same_list)):
##            pass # 여기 채워야 함.
##        serial = serial[:i-len(comp)] + same_list + serial[i:]
##        print("same_list", same_list)
##    # clen, comp 초기화
##    if (i <= n-1):
##        clen = len(serial[i])
##        comp = [serial[i]]
##    print(i, clen, comp)
##
### 3. 사전순
##pass
##
##serial.remove("")
##for j in range(n):
##    print(serial[j])
