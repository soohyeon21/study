# 26768

# 한 글자씩 확인해서 result에 한 글자씩 더하면 시간초과. 차라리 바로바로 print 하든가.

import sys

before = sys.stdin.readline().replace("\n", '')

litera = 'aeios'
cyfra = '43105'
for i in range(5):
    before = before.replace(litera[i], cyfra[i])

print(before)
