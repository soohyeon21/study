# 5355

# edit 창이 아니라 shell 창에 #를 쓰는 건 문제없음.
# #과 그 다음에 입력하는 것들이 빨간색으로 나온다 해서 지레짐작하지 말자.

t = int(input())

for _ in range(t):
    cal = 0
    mars = list(input().split())
    for j in range(len(mars)):
        if (j == 0):
            cal = float(mars[0])
        if (mars[j] == '@'):
            cal *= 3
        if (mars[j] == '%'):
            cal += 5
        if (mars[j] == '#'):
            cal -= 7
    print("%.2f" %(cal))
