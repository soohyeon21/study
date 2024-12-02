# 1969

# atgc.items() 만 써도 충분

import sys

n, m = map(int, sys.stdin.readline().split())
dna = [sys.stdin.readline().rstrip() for _ in range(n)]

result = ""
hdist = 0
for th in range(m):
    atgc = {'A':0, 'T':0, 'G':0, 'C':0}
    for each in range(n):
        atgc[dna[each][th]] += 1
    
    order = sorted(list(atgc.items()), key=lambda x:(-x[1], x[0]))
    result += order[0][0]
    hdist += n-order[0][1]

print(result)
print(hdist)
