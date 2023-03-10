# 6764

# 문제를 꼼꼼히 읽자.
# 4개 숫자가 동일하면 "Fish At Constant Depth"를 출력해야 한다.
# "strictly increasing/decreasing" => 증가/감소할 때 숫자가 모두 달라야 한다.

import sys

depth = [int(sys.stdin.readline()) for x in range(4)]
descending = sorted(depth, reverse=True)
ascending = sorted(depth)

state = ""
if (depth == [depth[0]]*4):
    state = "Fish At Constant Depth"
elif ((depth == descending) and (len(set(depth)) == 4)):
    state = "Fish Diving"
elif ((depth == ascending) and (len(set(depth)) == 4)):
    state = "Fish Rising"
else:
    state = "No Fish"

print(state)
