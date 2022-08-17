# 2563

# 단순무식하게 전개하는 것도 일종의 방법ㅋㅋ

import sys

n = int(sys.stdin.readline())
paper = [[0 for x in range(100)] for k in range(100)]

for _ in range(n):
    l, d = map(int, sys.stdin.readline().split())
    for xcoord in range(l, l+10):
        for ycoord in range(d, d+10):
            paper[xcoord][ycoord] = 1

area = 0
for i in range(100):
    area += paper[i].count(1)
print(area)


#
# 하다가 중간에 그만둔 풀이.
# 겹치는 부분을 구해서 빼는 방법은 아무래도 여기서는 사용하기 어려운 듯 하다.
#
##import sys
##
##p = int(sys.stin.readline())
##papers = []
##for _ in range(p):
##    pair = (map(int, sys.stdin.readline().split()))
##    papers.append(pair)
##
##surplus = 0
##for i in range(p):
##    l, d = papers[i][0], papers[i][1]
##    for j in range(p):
##        if ((l < papers[j][0] < l+10) and (d < papers[j][1] < d+10)):
##            surplus += (10-(papers[j][0]-l)) * (10-(papers[j][1]-d))
##        elif ((l < papers[j][0] < l+10) and (d < papers[j][1]+10 < d+10)):
##            surplus += (10-(papers[j][0]-l)) * (papers[j][1]-d)
##        elif ((l < papers[j][0]+10 < l+10) and (d < papers[j][1] < d+10)):
##            surplus += (papers[j][0]-l) * (d-papers[j][1])
##        elif ((l < papers[j][0]+10 < l+10) and (d < papers[j][1]+10 < d+10)):
##            surplus += (papers[j][0]-l) * (papers[j][1]-d)
        
