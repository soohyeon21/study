# 9196

# "입력으로 주어진 넓은 정수 직사각형보다 큰 직사각형 중 가장 작은 넓은 '정수 직사각형'의 높이와 너비를 출력한다."

# 1차는 대각선의 길이 기준, 2차는 높이 기준이기 때문에 height와 width는 h와 w보다 작을 수도 있다.

# 시간이 더 빠른 풀이도 더 있는듯.

import sys

while (1):
    h, w = map(int, sys.stdin.readline().split())
    if (h == w == 0):
        break

    dia2 = h**2 + w**2
    smallhw = []
    for height in range(1, 151):
        for width in range(1, 151):
            bigger_dia2 = height**2 + width**2
            if (((height==h) and (width==w)) or (width <= height) or ((bigger_dia2 == dia2) and (height < h))):
                continue
            if (bigger_dia2 >= dia2):
                smallhw.append((height, width, bigger_dia2))
    smallhw.sort(key=lambda x:(x[2], x[0]))
    print(smallhw[0][0], smallhw[0][1])
