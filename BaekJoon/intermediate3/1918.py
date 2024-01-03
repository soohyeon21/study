# 1918

### 중위 표기식 -> 후위 표기식
# 1) 숫자면 res에 넣기
# 2) "("이면 stack에
# 3) *, /이면 이미 stack에 있는 *, / 다 넣고 stack에 본인 추가
# 4) +, -이면 이미 stack에 있는 *, / 다 넣고 stack에 본인 추가 (단, 괄호 '(' 전까지만)
# 5) ")"이면 "("까지 stack에서 모두 pop
# 6) stack 모두 pop해서 비우기

import sys

equ = sys.stdin.readline().rstrip()

res = ""
stack = []
for e in equ:
    if (e.isalpha()):
        res += e
    elif (e == "("):
        stack.append(e)
    elif ((e == "*") or (e == "/")):
        while (stack and ((stack[-1] == "*") or (stack[-1] == "/"))):
            res += stack.pop()
        stack.append(e)
    elif ((e == "+") or (e == "-")):
        while (stack and (stack[-1] != "(")):
            res += stack.pop()
        stack.append(e)
    elif (e == ")"):
        while (stack and (stack[-1] != "(")):
            res += stack.pop()
        stack.pop()

while (stack): # 남은 애들 pop
    res += stack.pop()

print(res)
