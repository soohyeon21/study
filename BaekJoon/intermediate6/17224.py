# 17224

#
# sol1) sub2 작은 순서대로 sort, 남은 수만큼 sub1에서 고르기 위해서 푼 문제 제외하고 sub1 기준 sort
#
##import sys
##
##n, l, k = map(int, sys.stdin.readline().split())
##
##prob = []
##for q in range(n):
##    sub1, sub2 = map(int, sys.stdin.readline().split())
##    prob.append((q, sub1, sub2))
##
##cnt2, cnt1, left = 0, 0, k
##idx = []
##prob.sort(key=lambda x:(x[2], x[1]))
##for i in range(k):
##    if (prob[i][2] <= l):
##        cnt2 += 1
##        left -= 1
##        idx.append(i)
##
##new = []
##for j in range(n):
##    if (j not in idx):
##        new.append(prob[j])
##        
##new.sort(key=lambda x:x[1])
##for p in range(left):
##    if (new[p][1] <= l):
##        cnt1 += 1
##
##print(cnt2*140 + cnt1*100)



#
# sol2) 문제의 난이도가 L보다 작기만하면 상관없다. 따라서 그냥 sort 한 번만 해주고, k번 맞췄는지만 판단.
#
import sys

n, l, k = map(int, sys.stdin.readline().split())

prob = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
prob.sort(key=lambda x:x[1])

total = 0
cnt = 0
for i in range(n):
    if (cnt == k):
        break
    
    if (prob[i][1] <= l):
        total += 140
        cnt += 1
    elif (prob[i][0] <= l):
        total += 100
        cnt += 1

print(total)
