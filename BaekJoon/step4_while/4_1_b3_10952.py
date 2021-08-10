# 10952

# 둘 다 잘 작동한다.
# 2nd 풀이에서, break는 if문이 아니라 while문을 벗어나게 한다.

a, b = map(int, input().split())
lst = []

while((a != 0) and (b != 0)):
    lst.append(a + b)
    a, b = map(int, input().split())
    
for i in lst:
    print(i)

##import sys
##
##while(1):
##    a, b = map(int, sys.stdin.readline().split())
##    if ((a == 0) and (b == 0)):
##        break
##    print(a + b)
