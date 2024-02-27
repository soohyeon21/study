# 25640

import sys

jinho = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())

mbti = {jinho:0} # 진호 혼자인 경우도 포함
for _ in range(n):
    friend = sys.stdin.readline().rstrip()
    mbti[friend] = mbti.setdefault(friend, 0)
    mbti[friend] += 1

print(mbti[jinho])
