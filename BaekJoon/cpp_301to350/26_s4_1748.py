# 1748

# 1~9: 9개*1
# 10~99: 90개*2
# 100~999: 900개*3
# 1000~9999: 9000개*4

# 대충 방법은 생각해냈다.
# 9, 99, 999, ...도 있지만 (10-1), (100-1), (1000-1), ...로 볼 수도 있다는 점.

import sys

n = sys.stdin.readline().rstrip()
digit = 0
for i in range(len(n) - 1):
    digit += 10**i*9*(i+1)
digit += (int(n) - (10**(len(n)-1)-1))*len(n)

print(digit)


#
# 맞는 것 같은데, 왜 틀렸다지??
#
##import sys
##
##n = int(sys.stdin.readline())
##
##digit = 0
##for i in range(9):
##    if (n < 10**i*9):
##        elev = "1"*i
##        if (elev == ""):
##            elev = 0
##        else:
##            elev = int(elev)
##        digit += (n - elev*9)*(i+1)
##        break
##    digit += 10**i*9*(i+1)
##
##print(digit)    


#
# 맞는 누군가의 풀이
#
##n = input()
##result = 0
##for i in range(1,len(n)):
##    result+=9*10**(i-1)*i
##result +=(int(n)-10**(len(n)-1)+1)*len(n)
##print(result)


#
# 너무 느림
#
##import sys
##
##n = int(sys.stdin.readline())
##
##sst = ""
##for i in range(1, n+1):
##    sst += str(i)
##print(len(sst))
