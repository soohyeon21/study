# 15406

import sys

bill = sys.stdin.read().rstrip().split('\n')

total = 0
for i in range(len(bill)//2-1):
    each, cnt = map(int, bill[i*2+1].split())
    total += each*cnt

if (total >= int(bill[-1])):
    print('PAY')
else:
    print('PROTEST')
