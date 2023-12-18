# 16499

# "그룹에 속한 단어는 모두 같은 알파벳으로 이루어져 있어야 하고, 개수도 같아야 한다. 즉, 단어를 구성하는 알파벳의 순서만 달라야 한다."

# {{1, 2, 3}, {2, 1, 3}}처럼 set안에 set을 넣으면 "TypeError: unhashable type: 'set'"가 발생한다.

import sys

n = int(sys.stdin.readline())
groups = []
for _ in range(n):
    word = sorted(list(sys.stdin.readline().rstrip()))
    if (word not in groups):
        groups.append(word)

print(len(groups))
