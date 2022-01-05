# 1920

# 이진 탐색
# 다시 범위 설정 시에 median값은 포함하지 않도록 해야
# RecursionError: maximumm recursion depth exceeded in comparison이 발생하지 않는다.

# 입력값을 무조건 list로 만들어야 되는 것은 아니다. map()으로 끝내도 괜찮다.

import sys

def binary(find_at, start, end, me):
    if (start > end):
        return 0
    
    median = (start + end) // 2
    if (me == find_at[median]):
        return 1
    elif (me < find_at[median]):
        return binary(find_at, start, median-1, me)
    else: # (me > find_at[median]):
        return binary(find_at, median+1, end, me)

    
n = int(sys.stdin.readline())
narr = list(map(int, sys.stdin.readline().split()))
snarr = sorted(narr)
m = int(sys.stdin.readline())
marr = list(map(int, sys.stdin.readline().split()))

for num in marr:
##    print(binary(snarr, 0, len(snarr)-1, num)) # 이왕이면 알기 쉽게
    find_at = snarr
    start = 0
    end = len(snarr) - 1
    me = num
    print(binary(find_at, start, end, me))



# 출력 초과
#
##import sys
##
##n = int(sys.stdin.readline())
##narr = set(sys.stdin.readline().split())
##m = int(sys.stdin.readline())
##marr = list(sys.stdin.readline().split())
##
##print(narr, marr)
##
##for num in marr:
##    if (num in narr):
##        print(1)
##    else:
##        print(0)
