# 11158

# "Your friend becomes angry whenever he reads the following words or sequences of words:"
# "In fact he becomes angry even when a word contains 'lol' as a substring"
# 'lol'의 개수만큼 count가 아니라, 'lol'이 포함되어 있으면 해당 단어에 대해 1번만 count

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    sen = sys.stdin.readline().rstrip()
    words = sen.split()
    
    cnt = 0
    word_set = ["u", "ur"]
    for word in words:
        if (word in word_set):
            cnt += 1

    ws = ["would of", "should of"]
    for i in range(len(words)-1):
        if (words[i]+" "+words[i+1] in ws):
            cnt += 1

    for word in words:
        if ("lol" in word): # 한 단어 안에 "lol" 있기만 하면 1번 count
            cnt += 1
    #cnt += sen.count("lol") # 한 단어여도 "lol" 개수만큼 count # 틀림

    print(cnt*10)
