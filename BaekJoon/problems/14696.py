# 14696

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a, *ttakji_a = map(int, sys.stdin.readline().split())
    b, *ttakji_b = map(int, sys.stdin.readline().split())
    
    star = [ttakji_a.count(4), ttakji_b.count(4)]
    circle = [ttakji_a.count(3), ttakji_b.count(3)]
    square = [ttakji_a.count(2), ttakji_b.count(2)]
    triangle = [ttakji_a.count(1), ttakji_b.count(1)]

    win = ''
    if (star[0] != star[1]):
        win = ['A', 'B'][star.index(max(star))]
    elif ((star[0] == star[1]) and (circle[0] != circle[1])):
        win = ['A', 'B'][circle.index(max(circle))]
    elif ((star[0] == star[1]) and (circle[0] == circle[1]) and (square[0] != square[1])):
        win = ['A', 'B'][square.index(max(square))]
    elif ((star[0] == star[1]) and (circle[0] == circle[1]) and (square[0] == square[1]) and (triangle[0] != triangle[1])):
        win = ['A', 'B'][triangle.index(max(triangle))]
    elif ((star[0] == star[1]) and (circle[0] == circle[1]) and (square[0] == square[1]) and (triangle[0] == triangle[1])):
        win = 'D'

    print(win)
