# 15722

# 왜 x, y, head에 대해 def 안에서 global 안붙여주면 함수에서 각 변수에 영향 줄 수 없는 걸까?

import sys

def go(toward):
    global x, y
    if (toward == "N"):
        y += 1
    elif (toward == "E"):
        x += 1
    elif (toward == "S"):
        y -= 1
    elif (toward == "W"):
        x -= 1
    return

def turn(now):
    global head
    idx = ("NESW".index(now)+1)%4
    head = "NESW"[idx]
    return

n = int(sys.stdin.readline())

head = "N"
sec = 0
x, y = 0, 0
edge = 0
k = 1
while (sec < n):
    go(head)
    edge += 1
    if (edge == k):
        turn(head)
    if (edge == k*2):
        turn(head)
        edge = 0
        k += 1
    sec += 1

print(x, y)
