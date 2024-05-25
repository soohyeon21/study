# 9956

import sys

def word_reverse(block):
    alpha_only = ""
    for b in block:
        if (b.isalpha()):
            alpha_only += b
    reversed_alpha_only = alpha_only[::-1]

    idx = 0
    new_block = ""
    for i in range(len(block)):
        if (block[i].isalpha()):
            new_block += reversed_alpha_only[idx]
            idx += 1
        else:
            new_block += block[i]

    return new_block
    

while (1):
    line = sys.stdin.readline().replace("\n", "")
    if (line == "#"):
        break

    rst = ""
    word = ""
    cap = [0 for _ in range(len(line))]
    for k in range(len(line)):
        if (line[k].isspace()):
            rst += word_reverse(word)            
            word = ""
            rst += " "
        else:
            if (line[k].isupper()):
                cap[k] = 1
            word += line[k].lower()
            
    rst += word_reverse(word)

    final = ""
    for i in range(len(line)):
        final += rst[i] if cap[i]==0 else rst[i].upper()

    print(final)
