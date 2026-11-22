# 120849
# 모음 제거

def solution(my_string):
    vowel = 'aeiou'
    for letter in vowel:
        my_string = my_string.replace(letter, '')
    
    return my_string
