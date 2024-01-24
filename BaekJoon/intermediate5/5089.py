# 5089

# ㅎ... 문제를 꼼꼼히 잘 읽자.
# 'Week (몇번째 week) (중복 제외 마을 개수)' 이다.
# 중복이 몇 번 이루어졌는지를 구하는 것이 아니다. 따라서 dict.setdefault()는 과했달까.

import sys

tcase = 0
while (1):
    tcase += 1
    n = int(sys.stdin.readline())
    
    if (n == 0):
        break
    
    towns = {}
    for _ in range(n):
        town = sys.stdin.readline().rstrip()
        towns[town] = towns.setdefault(town, 0)
        towns[town] += 1

    print(f"Week {tcase} {len(towns)}")
