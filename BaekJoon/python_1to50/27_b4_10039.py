# 10039

# int() 쓸 바에야 / 말고 //를 써버렸다.

aa= []

for _ in range(5):
    score = int(input())
    if (score < 40):
        aa.append(40)
    else:
        aa.append(score)

avg_aa = sum(aa) // 5
print(avg_aa)
