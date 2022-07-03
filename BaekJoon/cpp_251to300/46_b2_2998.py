# 2998

# int(수, 2)이면 2진수로 받는다.
# oct() # 8진수 변환 함수

# 어휴 왜 틀렸지.. => '101'처럼 len()이 3으로 나누어 떨어지는 경우가 문제였다. 앞에 '0'이 붙어버린달까.
# eventually, rst에 int() 씌우는 거로 해결!! 오예~

# 그치만, 내가 구현하는 것보다는, 이미 있는 걸 사용하는게 더 좋은 거려나ㅎ


#
# sol1 (맞는 풀이)
#
import sys

num = sys.stdin.readline().rstrip()
many = 3 - (len(num) % 3)
num = "0" * many + num

octo = {"000":0, "001":1, "010":2, "011":3, "100":4, "101":5, "110":6, "111":7}
rst = ""
for i in range(len(num)//3):
    val = str(octo[num[i*3:i*3+3]])
    rst += val

print(int(rst))

#
# sol2 (맞는 풀이)
#
##import sys
##
##print(oct(int(sys.stdin.readline(), 2))[2:])
