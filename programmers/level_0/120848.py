# 120848
# 팩토리얼

def solution(n):
    fact = [1, 1]
    for k in range(2, 12):
        fact.append(fact[k-1]*k)
    
    for p in range(2, 12):
        if (fact[p-1] <= n < fact[p]):
            return p-1
