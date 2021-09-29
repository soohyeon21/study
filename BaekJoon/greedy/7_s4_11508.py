# 11508 2+1 세일

# 한 묶음 내에서 제일 싼 것을 무료로 준다면,
# 비싼 순으로 늘어놓고 앞에서부터 세 개씩 묶어주는 게 제일 좋다.
# 짝을 이루지 못한(제일 싼거 1개 or 제일 싼거 2개) 애들은 마지막에 잊지 않고 더해준다.

# sorted()와 list(reverse())를 사용해봤다.
# range(a, b, c) # a이상 b미만 c의 간격으로
# list[-5] # 음수도 가능하다. 뒤에서부터 -1, -2, ..., -n

n = int(input())
dairy = []

for _ in range(n):
    dairy.append(int(input()))

sett = n // 3 # 얘는 없어도 되겠다.
remain = n % 3

dairy_r = list(reversed(sorted(dairy)))

price = 0
for i in range(0, (n - remain), 3):
    price += dairy_r[i] + dairy_r[i + 1]

for j in range(1, (remain + 1)):
    price += dairy_r[-1 * j]

print(price)
