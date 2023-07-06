# 4118

# dictionary 생성할 때도 list처럼 for 사용할 수 있다.

# 확실히, dictionary가 빠르다.

# 해시 테이블이 빠른 이유
# => 저장할 때 key 값에 해시 함수를 적용해 고유한 index를 만들어 저장하기 때문.
#    key를 알면 해시 함수를 통해 바로 index를 알 수 있으므로 데이터를 찾을 때 O(1)의 평균 시간복잡도로 삭제, 조회 등이 가능하다.

import sys

while (1):
    num = int(sys.stdin.readline())
    if (num == 0):
        break

    lotto = {k:0 for k in range(1, 50)}
    for i in range(num):
        tmp = list(map(int, sys.stdin.readline().split()))
        for single in tmp:
            lotto[single] += 1

    values = lotto.values()
    if (0 in values):
        print("No")
    else:
        print("Yes")
