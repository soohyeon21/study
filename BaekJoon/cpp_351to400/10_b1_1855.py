# 1855

# 암호문을 만들때 왼쪽↔오른쪽 변경되는 것 주의

import sys

k = int(sys.stdin.readline())
encrypt = sys.stdin.readline().rstrip()
table = [[] for x in range(len(encrypt)//k)]

tmp = 0
for i in range(len(table)):
    for j in range(k):
        table[i].append(encrypt[tmp])
##        print(table, encrypt[tmp])
        tmp += 1
    if (i%2 == 1):
        table[i] = table[i][::-1]

rst = ""
for a in range(k):
    for b in range(len(table)):
        rst += table[b][a]

print(rst)
