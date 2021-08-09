# 2439

# (문자열).rjust(몇칸, 공백 대체 문자)
# (문자열)은 꼭 변수 형태 아니어도 됨. 그냥 따옴표로 묶인 문자열이어도 ok.

n = int(input())

for i in range(1, (n + 1)):
    a = "*" * i
    print(a.rjust(n))
##    a = "*" * i
##    print(("*" * i).rjust(n))


##n = int(input())
##
##for i in range(1, (n + 1)):
##    print(" " * (n - i) + "*" * i)
