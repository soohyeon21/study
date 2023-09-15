#2548

# 역시나, 통계 내용을 사용해야 했다.

#
# sol1)
# list에 존재하는 수 중에 대푯값이 있을 거라고 생각해서 하나씩 해본 방법
# 역시나 python3는 시간초과, pypy3는 정답
#
##import sys
##
##n = int(sys.stdin.readline())
##nlist = sorted(list(map(int, sys.stdin.readline().split())))
##
##whole = sum(nlist)
##rep = 10000
##for num in nlist:
##    comp = sum(abs(x-num) for x in nlist)
##    if (comp < whole):
##        rep = num
##        whole = comp
##    if (comp == whole):
##        rep = min(rep, num)
##
##print(rep)


#
# sol2) 중앙값 풀이
# python3로 정답. 시간&코드 길이 풀이 3개 중에 모두 제일 짧음.
# 중앙값(n이 홀수인 경우): (n+1)/2번째의 변량
# 중앙값(n이 짝수인 경우): n/2번째와 (n/2)+1번째의 변량의 (산술)평균
# 문제에서는 sum값이 동일하면 더 작은 수를 출력해야 하므로, n이 짝수여도 곧장 n/2번째만 고려해도 된다.
#
##import sys
##
##n = int(sys.stdin.readline())
##nlist = sorted(list(map(int, sys.stdin.readline().split())))
##
##if (n%2 == 1):
##    print(nlist[n//2])
##elif (n%2 == 0):
##    print(nlist[n//2-1])


#
# sol3) 이진 탐색
# python3로 정답.
#
import sys

n = int(sys.stdin.readline())
nlist = sorted(list(map(int, sys.stdin.readline().split())))

l, r = 0, n
whole = sum(nlist)
ans = nlist[-1]

while (l <= r):
    mid = (l+r)//2
    comp = sum(abs(num-nlist[mid]) for num in nlist)
    
    if (comp <= whole):
        r = mid-1
        whole = comp
        ans = min(ans, nlist[mid])
    elif (comp > whole):
        l = mid + 1

print(ans)
