# 9020

# 강한 골드바흐의 추측(Strong Goldbach Conjecture): 2보다 큰 모든 짝수는 두 소수의 합으로 표현가능하다.

#
# sol1) 시간초과. n이하 소수를 모두 찾아 가능한 순서쌍 만들어 확인하기
#
##import sys
##
### 10000까지의 수 중에서 소수 찾기
##prime = [1 for _ in range(10001)]
##prime[0], prime[1] = 0, 0
##
##for i in range(2, int(10000**0.5)+2):
##    for j in range(2, 10000//i+1):
##        prime[i*j] = 0
##
### 각 케이스 별로
##t = int(sys.stdin.readline())
##for _ in range(t):
##    n = int(sys.stdin.readline())
##    
##    # n이하 소수 찾기
##    prime_list = []
##    for k in range(n):
##        if (prime[k] == 1):
##            prime_list.append(k)
##
##    # 골드바흐 파티션 찾기
##    gold = []
##    for p1 in range(len(prime_list)):
##        for p2 in range(p1, len(prime_list)):
##            if (prime_list[p1]+prime_list[p2] == n):
##                gold.append((prime_list[p1], prime_list[p2], prime_list[p2]-prime_list[p1]))
##    gold.sort(key=lambda x:x[2])
##
##    print(gold[0][0], gold[0][1])



#
# sol2) n//2부터 +-1씩 하면서 만족하는 소수 찾기
# n의 골드바흐 파티션은 n/2으로부터 떨어진 거리가 항상 동일한가?
# n/2-k가 소수라고 가정할때, n/2+k도 소수인가?
#
import sys

def isPrime(num):
    if (num == 1):
        return False
    for k in range(2, int(num**0.5)+1): # num의 제곱근까지만 계산하므로 2,3,5,7 등의 소수를 걱정하지 않아도 된다.
        if (num % k == 0):
            return False
    return True

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    
    left, right = n//2, n//2
    for i in range(n//2):
        if (isPrime(left) and isPrime(right)):
            print(left, right)
            break
        else:
            left -= 1
            right += 1
