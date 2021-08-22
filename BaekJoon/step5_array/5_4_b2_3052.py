# 3052

# 같은 사람이 작성한 코드여도, 동일할 수는 없는 듯.
# set(): 중복 제거. 순서 없음.

a = []

for i in range(10):
    num = int(input())
    if (num % 42 not in a):
        a.append(num % 42)
#print(a)
print(len(a))
