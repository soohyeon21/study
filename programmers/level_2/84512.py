# 84512
# 모음 사전

###
### sol1) 모든 가능한 조합 만들어서 직접 word 순서 찾기
###
##def solution(wonder):
##    vowel = set()
##    
##    word = ['']*5
##    for w1 in 'AEIOU':
##        word[0] = w1
##        for w2 in 'AEIOU ':
##            word[1] = w2
##            for w3 in 'AEIOU ':
##                word[2] = w3
##                for w4 in 'AEIOU ':
##                    word[3] = w4
##                    for w5 in 'AEIOU ':
##                        word[4] = w5
##                        vowel.add(''.join(word).replace(' ', ''))
##    
##    vowel = sorted(list(vowel))
##    
##    return vowel.index(wonder)+1



###
### sol2) 규칙(w/등비수열의 합) 찾아서 적용
### A____: A + A_ + A__ + A___ + A____ → 1+5+5**2+5**3+5**4 = 781
### A___ : A + A_ + A__ + A___ → 1+5+5**2+5**3 = 156
### A__  : A + A_ + A__ → 1+5+5**2 = 31
### A_   : A + A_ → 1+5 = 6
### A    : A → 1 = 1
###
def geoSum(n): # 등비수열의 합 공식
    a = 1
    r = 5
    return a*(r**n - 1)//(r-1)

def solution(word):
    vowel = 'AEIOU'
    cores = [geoSum(num) for num in reversed(range(1, 6))] # [781, 156, 31, 6, 1]
    order = 0
    for i in range(len(word)):
        order += vowel.index(word[i]) * cores[i] + 1
    
    return order
