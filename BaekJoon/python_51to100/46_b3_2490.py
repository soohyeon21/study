# 2490

# 아스키 코드를 이용한 풀이도 있다. 확실히 길이가 짧아지긴 한다.

# ord() # 특정한 한 문자를 아스키 코드 값으로 변환해 주는 함수
# chr() # 아스키 코드 값을 문자로 변환해 주는 함수(10진수, 16진수 사용 가능)

# ord("@") == 64
# ord("A") == 65
# ord("B") == 66

# sol#1
for _ in range(3):
    yeut = list(map(int, input().split()))
    cnt = yeut.count(0)
    if (cnt == 1):
        print("A")
    elif (cnt == 2):
        print("B")
    elif (cnt == 3):
        print("C")
    elif (cnt == 4):
        print("D")
    else: # (cnt == 0)
        print("E")

# sol#2
# someone's code
# surprising solution
for _ in range(3):
    n = chr(list(map(int, input().split())).count(0) + 64)
    if (n == "@"):
        print("E")
    else:
        print(n)
