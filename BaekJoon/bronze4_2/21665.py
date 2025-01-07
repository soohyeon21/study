# 21665

# n x m 크기의 흑백 이미지와 반전시킨 흑백 이미지가 주어질때, 잘못 반전된 부분의 개수를 구하라.

# 이런 방법도 가능
# sum(A[i][j] == B[i][k] for i in range(n) for j in range(m))

import sys

def compare(ori, rev):
    cnt = 0
    for r in range(n):
        for c in range(m):
            if (ori[r][c] == rev[r][c]):
                cnt += 1
    return cnt


n, m = map(int, sys.stdin.readline().split())
original = [sys.stdin.readline().rstrip() for _ in range(n)]
blank = input()
reversal = [sys.stdin.readline().rstrip() for _ in range(n)]

wrong = compare(original, reversal)
print(wrong)
