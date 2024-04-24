# 15593

# 해고 없이 모두 근무할 때 시간표 # time
# 한 명씩 제외한 시간표 # change, without
# 제외한 시간 모음 # possible

#
# sol1) 전체 근무시간 측정 후 한 명씩 돌아가면서 해고했을 때 시간 측정
#
##import sys
##
##n = int(sys.stdin.readline())
##life = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
##
##time = [0 for x in range(1001)]
##for work in life:
##    for i in range(work[0], work[1]):
##        time[i] += 1
##
##possible = []
##for fire in life:
##    change = time.copy()
##    for j in range(fire[0], fire[1]):
##        change[j] -= 1
##
##    cnt = 1001 - change.count(0)
##    possible.append(cnt)
##
##print(max(possible))



#
# sol2) 돌아가면서 해고한 사람 제외하고 나머지 근무시간 측정
#
import sys

def time_except(person):
    without = [0 for x in range(1001)]
    for guard in life:
        if (guard == person):
            continue
        for t in range(guard[0], guard[1]):
            without[t] = 1
    return 1001 - without.count(0)
    

n = int(sys.stdin.readline())
life = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

possible = []
for fire in life:
    possible.append(time_except(fire))

print(max(possible))
