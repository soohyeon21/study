# 4299

# 입력에서 "축구 점수는 항상 음이 아닌 정수이고, 합과 차는 1000보다 작거나 같은 음이 아닌 정수이다." 조건도 코드에 포함시켜야 했다.
# 각 점수가 정수인지 판별하는 방법에 (add+sub)%2를 사용하는 방법도 있다.


import sys

add, sub = map(int, sys.stdin.readline().split())
if ((add < sub) or ((add+sub)%2)):
    print(-1)
else:
    a = (add+sub)//2
    b = add - a
    print(max(a, b), min(a, b))
