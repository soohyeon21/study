# pg.99 #3 1이 될 때까지

# k로 나눠지면 k로 나누고, 안 나눠지면 -1 하고.
# 풀이 과정이 해설과 좀 다른 듯 한데, 결국 같은 말 아닌가?

n, k = map(int, input().split())
cnt = 0

while (n != 1):
    if (n % k == 0):
        n //= k
        cnt += 1
    else: # n % k != 0
        n -= 1
        cnt += 1
print(cnt)
