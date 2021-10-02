# 1541 잃어버린 괄호

# - 뒤~ + 앞에 있는 수들을 괄호로 묶어버리면, 계산 시 가장 작은 수를 만들 수 있다.

# 풀이1
# -와 +를 기준으로 list에 연산자와 피연산자를 순서대로 분리하여 넣어준다.
# list의 뒤에서부터 -/+/숫자로 경우를 나누어
# -일 때는 더한 값들을 추가해주고
# +일 때는 제거해주고
# 숫자일 때는 값을 더해준다.
# 마지막에 보면, 앞쪽에 +만, 뒷쪽에 -만 모여있다.
# 연산자에 따라 +/-를 해주면 된다.

# 풀이2
# split("-")를 기준으로 하면 ['5', '4+5', '6+1'] 이런 형태가 된다.
# ['5', '9', '7'] 이런 형태가 되도록 요소 내에서는 더해준다.
# 첫 요소만 더해주고, 나머지 요소들은 빼주면 된다.

# python의 list는 자료형이 다른 것도 하나의 list에 넣을 수 있다.

# insert(a, b) # a번째 앞에 b를 삽입. 즉, b가 list의 a번째 요소가 된다.


# 풀이1
eq = input()
eqlst = []
cur = 0

# list로 분리하기
for i in range(len(eq)):
    if ((eq[i] == "-") or (eq[i] == "+")):
        eqlst.append(int(eq[cur:i]))
        eqlst.append(eq[i])
        cur = i + 1
eqlst.append(int(eq[cur:]))
##print(eqlst)

val = 0
wd = len(eqlst)
wd1 = wd - 1
for i in range(wd):
    if (eqlst[wd1 - i] == "-"):
        eqlst.insert((wd - i), val)
        val = 0
    elif (eqlst[wd1 - i] == '+'):
        eqlst.pop(wd1 - i)
    elif (eqlst[wd1 - i] != "+"):
        val += eqlst[wd1 - i]
        eqlst.pop(wd1 - i)
##    print(eqlst)
eqlst.insert(0, val)
##print(eqlst)

for k in range(1, len(eqlst), 2):
    if (eqlst[1] == "+"):
        eqlst[0] += eqlst[2]
        eqlst.pop(2)
        eqlst.pop(1)
    elif (eqlst[1] == "-"):
        eqlst[0] -= eqlst[2]
        eqlst.pop(2)
        eqlst.pop(1)
print(eqlst[0])



# 풀이2
##eq = input().split("-")
##
##arr = []
##
##for val in eq:
##    seg = val.split("+")
##    k = 0
##    for block in seg:
##        k += int(block)
##    arr.append(k)
##
##rtn = arr[0]
##for i in range(1, len(arr)):
##    rtn -= arr[i]
##print(rtn)

