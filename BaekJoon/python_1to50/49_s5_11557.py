# 11557

# string/int 서로 다른 자료형의 input()은 그냥 map() 말고 input()만.
# 그러면 다 string으로 인식되어 입력받을 수 있다.

t = int(input())

for _ in range(t):
    n = int(input())
    anss = None
    cnt = 0
    for _ in range(n):
        school, amount = input().split()
        if (cnt < int(amount)):
            anss = school
            cnt = int(amount)
    print(anss)
