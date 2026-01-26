# 35122

# 2개의 자연수의 자릿수가 같은 경우
# 2개의 자연수의 자릿수가 1 차이나는 경우

# or 오른쪽 자연수는 반드시 10의 배수가 됨.

import sys

n = int(sys.stdin.readline())

left = n//2 if (n%2==0) else n//2+1
right = n//2

rleast = int('1'+'0'*(len(str(right))-1))
left += right - rleast

rleast2 = int('1'+'0'*len(str(right)))
left2 = n - rleast2 if (n-rleast2>0) else 0

whole = int(str(left) + str(rleast))
if (left2 > 0):
    whole = max(whole, int(str(left2)+str(rleast2)), int(str(rleast2)+str(left2)))
    
print(whole)
