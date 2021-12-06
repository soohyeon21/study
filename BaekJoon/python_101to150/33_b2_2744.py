# 2744

# .swapcase() .upper() .lower() # 바꿔주는 함수들
# .isupper() .islower() # True/False를 return 값으로.

def switch_capital_small(input_word):
    new_word = ""
    for alphabet in input_word:
        if (97 <= ord(alphabet) <= 122):
            new_word += chr(ord(alphabet) - 32)
        else:
            new_word += chr(ord(alphabet) + 32)
    return new_word

import sys

word = sys.stdin.readline().rstrip()

print(switch_capital_small(word))
