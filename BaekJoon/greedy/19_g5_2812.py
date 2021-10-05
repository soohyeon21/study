# 2812 크게 만들기

# 짜증나. 1시간 넘게 매달렸는데.
# 답은 맞게 나오는데 시간초과여서 틀린다.
# 아오 짜증나.
# 나중에 다시 이 문제를 봤을 때는 꼭 풀 수 있으면 좋겠다.
# 대부분(아마 모든)의 풀이가 stack을 사용하는 것 같던데...

n, k = map(int, input().split())
num = input()

temp = [num[m] for m in range(k)]

for i in range(k):
    ind = num.find(min(temp))
    num = num[:ind] + num[ind+1:]
##    print(temp)
    temp.remove(min(temp))
    temp.append(num[k-1])

print(num)

##n, k = map(int, input().split())
##num = input()
##numr = [int(num[a]) for a in range(n)]
##
##temp = [numr[m] for m in range(k)]
##
##for i in range(k):
####    ele1 = temp.index(min(temp))
####    ele2 = numr.index(min(temp))
####    print(temp, numr)
####    del numr[ele1]
####    del temp[ele2]
##    numr.remove(min(temp))
##    temp.remove(min(temp))
##    temp.append(numr[k-1])
##
##ans = ''
##for j in range(len(numr)):
##    ans += str(numr[j])
##print(ans)
