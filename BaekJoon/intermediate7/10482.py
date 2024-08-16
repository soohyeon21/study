# 10482

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    x = int(sys.stdin.readline())
    
    primes = [True for y in range(x+1)]
    primes[0], primes[1] = False, False
    for i in range(2, int(x**0.5)+1):
        for j in range(2, x//i+1):
            primes[i*j] = False

    pairs = []
    for k in range(2, x//2+1):
        if (primes[k] and primes[x-k]):
            pairs.append((k, x-k))

    print(f"{x} has {len(pairs)} representation(s)")
    for pair in pairs:
        print(f"{pair[0]}+{pair[1]}")
    print()
