# 20006

# 아직 waiting 상태의 방이지만, +-10을 넘는 경우 고려
# m=1 고려

import sys

p, m = map(int, sys.stdin.readline().split())
room = {i:['', []] for i in range(p)}

for _ in range(p):
    l, n = sys.stdin.readline().split()
    l = int(l)
    for k, v in room.items():
        if (v[0] == ''):
            room[k][1].append((l, n))
            if (len(v[1]) == m):
                v[0] = 'Started!' # (m = 1)
            else:
                v[0] = 'Waiting!' # (m != 1)
            break
        elif (v[0] == 'Waiting!'):
            if (abs(v[1][0][0]-l) <= 10):
                room[k][1].append((l, n))
            else:
                continue
            if (len(room[k][1]) == m):
                room[k][0] = 'Started!'
            break

for k, v in room.items():
    if (v[0] != ''):
        print(room[k][0])
        for member in sorted(v[1], key=lambda x:x[1]):
            print(member[0], member[1])
