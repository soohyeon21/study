# 18110

# def round를 (num-int(num) < 0.5)로 판단해도 된다.
# math.floor(num+0.5)도 가능함.

#
# sol1)
# rest70 = rank[outlier15:-outlier15] # 이렇게 하면 3 이하의 n일때 len(rest70)=0이 된다.
#
import sys

def int_round(num):
    under1 = num%1
    if (under1 < 0.5):
        return int(num)
    else:
        return int(num)+1

n = int(sys.stdin.readline())
rank = sorted([int(sys.stdin.readline()) for _ in range(n)])

outlier15 = int_round(n*0.15)
rest70 = rank[outlier15:n-outlier15]
trim_avg = 0
if (n != 0):
    trim_avg = int_round(sum(rest70)/(n-outlier15*2))

print(trim_avg)


#
# sol2) 첫 풀이
# round를 사용하면 틀린다. round(4.5)가 4가 나옴!
#
##import sys
##
##def upORthrow(num):
##    if (5 <= int((num%1)*10)):
##        num += 1
##    return int(num)
##
##
##n = int(sys.stdin.readline())
##difficulty = sorted([int(sys.stdin.readline()) for _ in range(n)])
##
##excluding_num = upORthrow(n*0.15)
###excluding_num = round(n*0.15) # 틀린 풀이
##
##selected_difficulty = difficulty[excluding_num:n-excluding_num]
##
##tmean = 0
##if (len(selected_difficulty) != 0):
##    tmean = upORthrow(sum(selected_difficulty)/len(selected_difficulty))
##    #tmean = round(sum(selected_difficulty)/len(selected_difficulty)) # 틀린 풀이
##
##print(tmean)
