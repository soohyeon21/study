# 20300 서강근육맨

# 짝수인 경우와 홀수인 경우를 나누어 생각해야 한다.
# 짝수인 경우, 오름차순/내림차순을 짝끼리 더한 후 max 값이 답이다.
# 홀수인 경우, 제일 큰 수와, 나머지 수끼리 오름차순/내림차순 짝의 합을 구하고,
# 제일 큰 수와 짝의 합들 중에 max 값이 답이다.

# t가 sort된 애라고 생각하고 sort를 안해줬다. 나중에 ts 추가.
# (1, 1, 1, 1, 8)인 경우, 첫번째 풀이에서는 못 잡아낼 줄 알았다.
# 그래서 두 번째 풀이에는 ts의 마지막 원소를 더해줬는데,
# 사실 첫 번째 풀이에도 포함되어 있는 방법이었다,
# ts에 0을 추가해주는 것이, 제일 큰 마지막 원소를 살리는 방법이었다.
# 결국엔, 문제에는 문제가 없었고, 두 풀이도 같은 아이디어다.
# 그냥 두 번째 풀이에는 그닥 필요없는 한 줄이 추가되었다는 것 정도?

# a.pop(k) # list a에서 'k번째 값'을 없애준다.
# a.index(k) # list a에서 값 k의 index 값을 알려준다.
# 애초에 ts.pop(ts.index(ts[n-1])) 대신 ts.pop(n-1)해도 되었을 듯.

# pop()은 해당 값을 출력해주지는 않는다.
# pop()에 해당하는 값이 여러개 있으면, 그 중 하나만 없애준다.

# a.remove(k) # list a에서 'k값'을 없애준다.

# del a[j] # list a에서 a[j] 값을 삭제해 준다.

# 풀이1
n = int(input())
t = list(map(int, input().split()))

ts = sorted(t) # 오름차순
tr = list(reversed(sorted(t))) # 내림차순
##print(ts, tr)

even = []
odd = []

if (n % 2 == 0): # 짝수 개
    for i in range(n):
        even.append(ts[i] + tr[i])
    minm = max(even)
else: # 홀수 개
##    odd.append(ts[n - 1])
    ts.pop(ts.index(ts[n-1]))
    ts.append(0)
    ts.sort()
    for j in range(n):
        odd.append(ts[j] + tr[j])
    minm = max(odd)

##print(odd, even)
print(minm)


# 풀이 2
##n = int(input())
##t = list(map(int, input().split()))
##
##ts = sorted(t) # 오름차순
##tr = list(reversed(sorted(t))) # 내림차순
####print(ts, t)
##
##even = []
##odd = []
##
##if (n % 2 == 0): # 짝수 개
##    for i in range(n):
##        even.append(ts[i] + tr[i])
##    minm = max(even)
##else: # 홀수 개
##    odd.append(ts[n - 1])
##    ts.pop(ts.index(ts[n-1]))
##    ts.append(0)
##    ts.sort()
##    for j in range(n):
##        odd.append(ts[j] + tr[j])
##    minm = max(odd)
##
####print(odd, even)
##print(minm)
