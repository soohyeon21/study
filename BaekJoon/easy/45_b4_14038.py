# 14038

import sys

game = []
for _ in range(6):
    game.append(sys.stdin.readline().rstrip())
    
win = game.count('W')
if (win > 4):
    print(1)
elif (win > 2):
    print(2)
elif (win > 0):
    print(3)
else:
    print(-1)
