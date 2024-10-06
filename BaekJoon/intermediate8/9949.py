# 9949

# or replace()

import sys

idx = 1
while (1):
    underscore = sys.stdin.readline().split()
    if (underscore[0] == "#"):
        break

    n = int(sys.stdin.readline())
    
    print(f"Case {idx}")
    for _ in range(n):
        sentence = sys.stdin.readline().rstrip()
        for letter in sentence:
            if (letter.lower() in underscore):
                print("_", end='')
            else:
                print(letter, end='')
        print()
    idx += 1
    print()
