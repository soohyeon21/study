# 11948

# sort() 안하고 그냥 다 더한 다음에 각각의 min값 빼는 방법도 있다.

import sys

science = []
social = []

for i in range(4):
    science.append(int(sys.stdin.readline()))

for j in range(2):
    social.append(int(sys.stdin.readline()))

science.sort(reverse=True)
social.sort(reverse=True)

max_total = sum(science[:3]) + social[0]

print(max_total)
