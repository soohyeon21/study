# 7567

# out of range가 되지 않도록 주의하자

# 처음 시작할 때는 '('이든 ')'이든 무조건 10을 더해줘야 한다.
# 2번째 그릇부터 직전 그릇과 같은 방향인지 아닌지 판단하여 5 or 10을 더하도록 한다.

bowl = input()
h = 10

for i in range(1, len(bowl)):
    if (bowl[i - 1] == bowl[i]):
        h += 5
    else: # (bowl[i - 1] != bowl[i])
        h += 10

print(h)
