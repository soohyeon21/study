# 18063

# 곡의 길이가 c보다 짧은 경우 고려!

import sys

n, c = map(int, sys.stdin.readline().split())

hour, minute, second = 0, 0, 0
t = []
for _ in range(n):
    m, s = map(int, sys.stdin.readline().split(":"))
    t.append(m*60+s)

second = sum(t)
for i in range(1, n):
    second -= min(t[i-1], t[i], c)

minute = second//60
second %= 60
hour = minute//60
minute %= 60

print(f"{hour:02}:{minute:02}:{second:02}")
