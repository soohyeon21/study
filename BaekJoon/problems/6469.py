# 6469

# 아니면 더 간단하게, step과 mod의 최대공약수가 1이면 Good, 1보다 크면 Bad 이다.

import sys

while (1):
    ipt = sys.stdin.readline().rstrip()
    if (ipt == ''):
        break
    
    step, mod = map(int, ipt.split())

    seeds = {i:0 for i in range(mod)}
    seed = 0
    while (seeds[seed] == 0):
        seeds[seed] += 1
        seed = (seed + step) % mod

    state = 'Bad'
    if (sum(seeds.values()) == mod):
        state = 'Good'

    print(f"{step:>10}{mod:>10} {state} Choice\n")
