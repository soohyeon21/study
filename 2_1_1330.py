# 1330 두 수 비교하기

a, b = map(int, input().split())
if (a > b):
    print(">")
elif (a < b):
    print("<")
else:
    print("==")

## input().split(",") # 하면 , 기준으로 문자 구분.
## split(",") 하고 "1,2"든, "1, 2"든 모두 잘 돌아감.
