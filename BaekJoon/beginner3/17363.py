# 17363

# a = "abcde"
# a.translate(str.maketrans('abcde', 'fghij')) # dictionary or 같은 길이 문자열
# >>> 'fghij'
# a.translate(str.maketrans('abcde', 'fghij', 'c')) # 3rd argument for None
# >>> 'fgij'

import sys

left = {".":".", "O":"O", "-":"|", "|":"-", "/":"\\", "\\":"/", "^":"<", "<":"v", "v":">", ">":"^"}

n, m = map(int, sys.stdin.readline().split())
straight = [sys.stdin.readline().rstrip() for x in range(n)]

new = []
for line in straight:
    changed = ""
    for letter in line:
        changed += left[letter]
    new.append(changed)

for i in range(m-1, -1, -1):
    for j in range(n):
        print(new[j][i], end="")
    print()
