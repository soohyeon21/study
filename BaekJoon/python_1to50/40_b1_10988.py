# 10988

# 오, list의 reversed()를 사용하는 방법도 있다.

word = input()

drow = ''

for i in range(1, len(word) + 1):
    drow += word[-1 * i]

if (word == drow):
    print(1)
else:
    print(0)
