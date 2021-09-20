# 4101

# while 조건 안에 a, b가 0이 되는 것을 종료조건으로 넣어버리면
# 0, 0이 입력되었을 때에도 No를 출력해버린다.

a, b = -1, -1

while (1):
    a, b = map(int, input().split())
    if ((a == 0) and (b == 0)):
        break
    elif (a > b):
        print("Yes")
    else:
        print("No")
