# 2588

# input은 문자열로 저장한다.
# 문자열로 계산 vs 숫자로 바꾸어 계산

a = int(input())
b = input()

b3 = a * (int(b[2]))
b4 = a * (int(b[1]))
b5 = a * (int(b[0]))
b6 = b3 + b4 * 10 + b5 * 100

print(b3)
print(b4)
print(b5)
print(b6)
