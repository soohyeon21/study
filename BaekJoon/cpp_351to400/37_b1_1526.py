# 1526

# 반복문 안쓰려 해봤는데 안됐다.
# 기본적으로 반복문은 쓰되, 중간 과정을 어떻게 해결하는 지에 따라 시간이 덜 걸리기도 하는 듯.

import sys

n = sys.stdin.readline().rstrip()

while (1):
    nums = [n[x] for x in range(len(n))]
    if (nums.count("4") + nums.count("7") == len(nums)):
        break
    else:
        n = str(int(n) - 1)

print(n)

#
# 틀린 풀이
#
### 442 넣었을때 문제ㅎ
##import sys
##
##n = sys.stdin.readline().rstrip()
##km = ""
####minus = False
##
##if (int(n[0]) < 4): # 3입력하면 error 나지만, 입력 조건에 있으니까 패스
##    n = "9"*(len(n)-1)
##
##for i in range(len(n)-1):
####    if (minus):
####        km += "7"
####        minus = False
##        
##    # 7~
##    if (int(n[i]) > 7):
##        km += "7"
##        n = n[:i+1] + "9"*len(n[i+1:])
##    elif ((int(n[i]) == 7) and (int(n[i+1]) >= 7)):
##        km += "7"
##    elif ((int(n[i]) == 7) and (4 <= int(n[i+1]) < 7)):
##        km += "7"
##    elif ((int(n[i]) == 7) and (int(n[i+1]) < 4)):
##        km += "4"
##    # 4~7
##    elif (int(n[i]) > 4):
##        km += "4"
##        n = n[:i+1] + "9"*len(n[i+1:])
##    elif (int(n[i]) == 4):
##        if (int(n[i+1]) < 4):
####            minus = True
####            continue
##            
##            n = n[:i+1] + "9"*len(n[i+1:])
##        else:
##            km += "4"
##    # ~4
##    else:
##        n = n[:i+1] + "9"*len(n[i+1:])
####        minus = True
####        print(i, n[i])
####    print(km)
####print(km)
####if (int(n[-1]) >= 7):
####    km += "7"
####elif (int(n[-2]) > int(km[-1])):
####    km += 7
####elif (int(n[-2]) == int(km[-1])):
####    
####if (4 <= int(n[-1]) < 7):
####    km += "4"
####else:
####    km += "7"
##if (int(n[-1]) >= 7):
##    km += "7"
##elif (4 <= int(n[-1])):
##    km += "4"
##elif (int(n[-1]) < 4):
##    km += "7"
##else:
##    km += "0"
##
##print(km)
