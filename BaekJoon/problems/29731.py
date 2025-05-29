# 29731

import sys

rick = ['Never gonna give you up', 'Never gonna let you down', 'Never gonna run around and desert you', 'Never gonna make you cry', 'Never gonna say goodbye', 'Never gonna tell a lie and hurt you', 'Never gonna stop']

n = int(sys.stdin.readline())

state = True
for _ in range(n):
    hack = sys.stdin.readline().rstrip()
    if (hack not in rick):
        state = False

if (state):
    print("No")
else:
    print("Yes")
