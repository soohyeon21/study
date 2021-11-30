# 2822

# list1 = sorted(list, reverse=True) # 내림차순으로(정확히는 오름차순 뒤집어서) 정렬

# sorted()[x::] # sorted()[x:] # 동일한 의미인 듯. sort하고 x번째부터만 가져오기.

# from operator import itemgetter, attrgetter
# sorted(student_tuples, key=itemgetter(1,2))
# >>> [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

import sys

score = [int(sys.stdin.readline()) for _ in range(8)]
score1 = sorted(score, reverse=True)

order = []
for i in range(5):
    order.append(score.index(score1[i]) + 1)
order.sort()

print(sum(score1[:5]))
for order_num in order:
    print(str(order_num) +" ", end="")
