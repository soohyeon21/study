# 10808

# print(many[i], end=" ")하면 끝에 빈칸 하나 주고 이어서 출력해준다.

# chr()을 사용하는 풀이도 심심찮게 있더라. ASCII 코드!

s = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
many = []

for i in range(26):
    many.append(s.count(alpha[i]))

for cnt in many:
    print(str(cnt) + " ", end="")
