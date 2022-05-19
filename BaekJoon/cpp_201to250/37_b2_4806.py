# 4806

# sys.stdin.readline().rstrip()을 사용해버리면, 오른쪽 끝의 개행문자를 삭제한다.
# 그러나 문제에 '빈 줄이 주어질 수도 있다' 하였으므로, 그냥 input()을 사용하자.
# (그냥 sys에 '\n'만 삭제하는 작업을 추가해주면 될 수도?)

cnt = 0
while (1):
    try:
        s = input()
        cnt += 1
    except EOFError:
        break
print(cnt)
