# 15921

# 기대값: 새로운 데이터가 관측되었을 때, 그 데이터가 확률적으로 어떤 값을 가질지를 예측할 때
# 평균: 이미 구해진 값에 대하여 통계적인 특성을 분석할 때

# 결국 n이 0이 아닌 이상 결과값은 계산할 필요도 없이 "1.00"이다.

import sys

n = int(sys.stdin.readline())
if (n == 0):
    print("divide by zero")
else:
    print("1.00")
