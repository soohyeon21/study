# 9287

# 모든 층을 " "으로 간격을 두고 하나의 문자열로 합친 다음, "00"이 있는지 확인하는 방법도 있다.

# or any() 사용

import sys

t = int(sys.stdin.readline())
for idx in range(1, t+1):
    story = int(sys.stdin.readline())
    jenga = [sys.stdin.readline().rstrip() for x in range(story)]
    
    state = True
    for each in jenga:
        if ("00" in each):
            state = False
            
    print(f"Case {idx}: ", end='')
    if (state):
        print("Standing")
    else:
        print("Fallen")
