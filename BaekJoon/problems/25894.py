# 25894

import sys

n = int(sys.stdin.readline())
for tcase in range(1, n+1):
    print(f"Test case #{tcase}:")
    p = int(sys.stdin.readline())
    same = [tuple(sys.stdin.readline().split()) for _ in range(p)]

    q = int(sys.stdin.readline())
    for qi in range(q):
        test = sys.stdin.readline().rstrip()
        test_new = test
        for re_pair in same:
            test_new = test_new.replace(re_pair[0], re_pair[1])

        print(test, end=' ')
        if (test_new == test_new[::-1]):
            print("YES")
        else:
            print("NO")
    print()
