# 42885
# 구명보트

# L ≤ k1 ≤ k2 ≤ H 라고 할때,
# (① L+k2 ≤ limit, ② k1+H ≤ limit)이 (보트를 꽉 채운) 최적의 해라고 한다면,
# (① L+H ≤ limit, ② k1+k2 ≤ limit)도 여전히 성립한다.(= 꽉꽉 채우지 못할 뿐, 보트 개수는 유지된다.)
# ∵ (L+H ≤ k1+H ≤ limit), (k1+k2 ≤ k1+H ≤ limit)
# ∴ sorted에서 양끝의 element를 하나씩 점진적으로 확인해도 최적의 보트 수를 구할 수 있다.
# +) (L+H ≤ limit)이라고 해서 (k1+k2 ≤ limit)이 보장되지는 않는다. ex) 5-6-8-8, limit=13

## 최적화 대상을 clarify: 보트 하나 꽉꽉 채워서 개수 최소화(X), 보트 개수 최소화(O)

# Greedy: 매 순간 특정 기준에 따라 선택을 확정하면서 전체 문제를 해결하는 알고리즘.

def solution(people, limit):
    people = sorted(people)
    
    boat = 0
    left = 0
    right = len(people)-1
    while (left < right):
        if (people[left] + people[right] <= limit):
            left += 1
        right -= 1
        boat += 1
        
    if (left == right):
        boat += 1
    
    return boat
