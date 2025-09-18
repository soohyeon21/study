# 1063

# '=', '.copy()' 모두 얕은 복사라는데, 왜 여기서는 'ktmp=king'과 'ktmp=king.copy()' 했을때 결과가 다르게 나올까?
# 1차원 list를 .copy()하는 경우에는 '얕은 복사'이지만, '깊은 복사'처럼 작용함.

import sys

k, r, n = sys.stdin.readline().split()
king = [ord(k[0])-64, int(k[1])]
rock = [ord(r[0])-64, int(r[1])]

kmove = {'R':(1, 0), 'L':(-1, 0), 'B':(0, -1), 'T':(0, 1),
         'RT':(1, 1), 'LT':(-1, 1), 'RB':(1, -1), 'LB':(-1, -1)}

for _ in range(int(n)):
    move = sys.stdin.readline().rstrip()
    ktmp = king.copy()
    rtmp = rock.copy()
    
    ktmp[0] += kmove[move][0]
    ktmp[1] += kmove[move][1]
    if (ktmp == rtmp):
        rtmp[0] += kmove[move][0]
        rtmp[1] += kmove[move][1]

    if ((1 <= ktmp[0] <= 8) and (1 <= ktmp[1] <= 8) and (1 <= rtmp[0] <= 8) and (1 <= rtmp[1] <= 8)):
        king = ktmp
        rock = rtmp

final_k = chr(king[0]+64) + str(king[1])
final_r = chr(rock[0]+64) + str(rock[1])

print(final_k)
print(final_r)
