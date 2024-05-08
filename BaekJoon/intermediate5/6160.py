# 6160

# 굳이 dict 사용 안해도 ok
# result도 하나 가지고 계속 사용해도 ok

import sys

n, k = map(int, sys.stdin.readline().split())

vote1 = {}
vote2 = {}
for i in range(1, n+1):
    ai, bi = map(int, sys.stdin.readline().split())
    vote1[i] = ai
    vote2[i] = bi

result1 = sorted(list(vote1.items()), key=lambda x:-x[1])[:k+1]

result2 = []
for j in range(k):
    result2.append((result1[j][0], vote2[result1[j][0]]))
winner = sorted(result2, key=lambda x:-x[1])[0][0]

print(winner)
