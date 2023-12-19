# 12606

# f-string에는 *sen[::-1]와 같이 starred expression 사용 불가
# 쓸거면 따로 print() 안에 넣거나 ,로 따로 나열할 것.

import sys

n = int(sys.stdin.readline())
for i in range(1, n+1):
    sen = sys.stdin.readline().split()
    print(f"Case #{i}: {' '.join(sen[::-1])}")
