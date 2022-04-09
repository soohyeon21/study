# 2495

# 마지막 letter 수행 후, cnt를 max_cnt에 추가해줘야 한다.

# 예시가 간단하다면, 첫/끝 case에 대해 다 수행해보자.

import sys

for _ in range(3):
    s = sys.stdin.readline().rstrip()
    num = s[0]
    cnt = 1
    max_cnt = []
    
    for letter in s[1:]:
        if (num == letter):
            cnt += 1
        else:
            num = letter
            max_cnt.append(cnt)
            cnt = 1
    max_cnt.append(cnt)
    print(max(max_cnt))
