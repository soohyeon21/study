# 10102

# vote.count("A")
# 이런식으로 for문 돌리지 않고 count()를 사용하는 방법도 있다.
# tie와 Tie의 차이는 크다...ㅎ

v = int(input())
vote = input()

cnta = 0
cntb = 0

for i in range(v):
    if (vote[i] == "A"):
        cnta += 1
    else: # (vote[i] == "B")
        cntb += 1

if (cnta > cntb):
    print("A")
elif (cnta < cntb):
    print("B")
else: # (cnta == cntb)
    print("Tie")
