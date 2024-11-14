# 11059

# sum list를 구해서
# mid = start + length//2
# sum_front = sumList[mid] - sumList[start]
# sum_back = sumList[start + length] - sumList[mid]
# if (sum_front == sum_back)을 판단하는 방식으로 푸는 방법도 있다.
# 이렇게 되면 시간이 매우매우매우 빨라짐.

import sys

def longest(s):
    for length in reversed(range(1, len(s)+1)):
        if (length%2 != 0):
            continue
        for start in range(len(s)-length+1):
            part = s[start:start+length]
            if (sum(int(digit) for digit in part[:len(part)//2]) == sum(int(digit) for digit in part[len(part)//2:])):
                print(length)
                return


s = sys.stdin.readline().rstrip()

longest(s)
