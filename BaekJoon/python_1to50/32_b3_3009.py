# 3009

# 역시 사람에 따라 작성 방법은 다양한 듯 하다.
# x와 y를 구할 때 공통이 되는 부분이 있어서 함수 처리 했다.
# function은 parameter로 list를 받아 처리하는 것도 가능하다.

def findxy(point):
    for i in range(3):
        cnt = point.count(point[i])
        if (cnt == 1):
            return point[i]
            break

xp = []
yp = []

for _ in range(3):
    x, y = map(int, input().split())
    xp.append(x)
    yp.append(y)


print(findxy(xp), findxy(yp))
