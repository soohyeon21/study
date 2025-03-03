# 25955

# 굳이 wrong을 sort 해 줄 필요 없이, prob와 hard_order가 다른 애들을 출력해줘도 된다.
# 아니면 prob와 hard_order가 다른 경우, hard_order를 wrong에 순서대로 append하고 출력해도 됨.

import sys

n = int(sys.stdin.readline())
prob = sys.stdin.readline().split()

tier = {"B":1, "S":2, "G":3, "P":4, "D":5}
hard_order = [(prob[i], tier[prob[i][0]], int(prob[i][1:])) for i in range(n)]
hard_order.sort(key=lambda x:(x[1], -x[2]))

state = True
wrong = []
for j in range(n):
    if (prob[j] != hard_order[j][0]):
        state = False
        wrong.append((prob[j], tier[prob[j][0]], int(prob[j][1:])))

wrong.sort(key=lambda x:(x[1], -x[2]))

if (state):
    print("OK")
else:
    print("KO")
    for k in range(2):
        print(wrong[k][0], end=' ')
