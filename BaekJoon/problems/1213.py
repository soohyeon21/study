# 1213

import sys

def makePalindrome(name):
    alpha_dict = {x:name.count(x) for x in list(set(name))}
    
    remains = [v%2 for v in alpha_dict.values()]
    ## 홀수가 여러개 존재하는 경우
    if (sum(remains) > 1):
        return "I'm Sorry Hansoo"

    ## 홀수가 1개 이하로 존재하는 경우
    odd_alphabet = "" # 홀수개인 알파벳
    alpha_dict_one_odd = {}
    for k, v in alpha_dict.items():
        if (v%2 == 0):
            alpha_dict_one_odd[k] = v
        else:
            odd_alphabet = k
            alpha_dict_one_odd[k] = v-1

    pairs = sorted(list(alpha_dict_one_odd.items()), key=lambda x:x[0])
    answer = ""
    for one in pairs:
        answer += one[0] * (one[1]//2)
    return answer + odd_alphabet +answer[::-1]
    

name = sys.stdin.readline().rstrip()

result = makePalindrome(name)
print(result)
