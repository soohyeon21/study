# 14561

# convert()가 문제였다. jin이 11보다 커지면 ABCDE를 활용해야 한다.
# 어쩐지... print 부분은 맞는데 계속 틀려서 이상했다.

# dict 대신 "0123456789ABCDEF" 사용 가능
# 아니면 굳이 문자열로 만들 필요 없이 list에 담아도 된다. 그러면 ABCDEF 안쓰고 숫자 쓸 수 있다.

import sys

def convert(decimal, jin):
    result = ""
    digit = {x:str(x) for x in range(10)}
    digit[10] = "A"
    digit[11] = "B"
    digit[12] = "C"
    digit[13] = "D"
    digit[14] = "E"
    digit[15] = "F"
    while (decimal != 0):
        result = digit[decimal%jin] + result
        decimal //= jin
    return result

t = int(sys.stdin.readline())
for _ in range(t):
    a, n = map(int, sys.stdin.readline().split())
    str_num = convert(a, n)

    # way1
    if (str_num[:len(str_num)//2] == str_num[-(len(str_num)//2):][::-1]):
        print(1)
    else:
        print(0)
    # way2
##    state = True
##    for i in range(len(str_num)//2):
##        if (str_num[i] != str_num[len(str_num)-1-i]):
##            state = False
##    if (state):
##        print(1)
##    else:
##        print(0)
