# 2530

# h, m, s에 바로 바뀐 값을 넣어버리면, 밑에서 해당 변수를 사용함에 문제가 생길 수 있다.
# 변수에 저장된 값이 변해도 되는지 않되는지 판단하자.

h, m, s = map(int, input().split())
d = int(input())
sdsum = s + d

s1 = sdsum % 60
m1 = ((sdsum // 60) + m) % 60
h1 = ((((sdsum // 60) + m) // 60) + h) % 24
print(h1, m1, s1)
##print(sdsum, (sdsum // 60), ((sdsum // 60) + m), ((sdsum // 60) + m) % 60)
