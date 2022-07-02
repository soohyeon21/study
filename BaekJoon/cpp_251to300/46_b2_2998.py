# 2998

# int(수, 2)이면 2진수로 받는다.
# oct() # 8진수 변환 함수
# 어휴 왜 틀렸지..

##import sys
##
##num = sys.stdin.readline().rstrip()
##many = 3 - (len(num) % 3)
##num = "0" * many + num
##
##octo = {"000":0, "001":1, "010":2, "011":3, "100":4, "101":5, "110":6, "111":7}
##rst = ""
##for i in range(len(num)//3):
##    val = str(octo[num[i*3:i*3+3]])
##    rst += val
##
##print(rst)

import sys

print(oct(int(sys.stdin.readline(), 2))[2:])
