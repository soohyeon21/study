# 9324

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    msg = sys.stdin.readline().rstrip()

    many = {}
    before = ""
    for letter in msg:
        many[letter] = many.setdefault(letter, 0)
        many[letter] += 1
        if (many[letter] == 3):
            many[letter] = 0
        else:
            before += letter

    many = {}
    real = ""
    for letter in before:
        many[letter] = many.setdefault(letter, 0)
        many[letter] += 1
        if (many[letter] == 3):
            real += letter
            many[letter] = 0
        real += letter
        
##    object_strs = [msg, before, real]
##    for i in range(2):# in object_strs:
##        many = {}
##        for letter in object_strs[i]:
##            many[letter] = many.setdefault(letter, 0)
##            many[letter] += 1
##            if (i == 0):
##                print(letter, many[letter])
##                if (many[letter] == 3):
##                    many[letter] = 0
##                else:
##                    object_strs[i+1] += letter
##            elif (i == 1):
##                pass
##            if (many[letter] == 3):
##                many[letter] = 0
##            else:
##                object_strs[i+1] += letter

    #print(f"msg: {msg}, before: {before}, real:{real}")
    if (msg == real):
        print("OK")
    else:
        print("FAKE")
            


        
##    for letter in msg:
##        many[letter] = many.setdefault(letter, 0)
##        many[letter] += 1
##        if (many[letter] == 3):
##            many[letter] = 0
##        else:
##            before += letter
##
##    for letter in before:
