# 4659

import sys

while (1):
    pw = sys.stdin.readline().rstrip()
    if (pw == 'end'):
        break

    vow_state = False
    for vow in 'aeiou':
        if (vow in pw):
            vow_state = True

    seq3 = True
    for cri in range(len(pw)-2):
        vow, cons = 0, 0
        for tri in range(cri, cri+3):
            if (pw[tri] in 'aeiou'):
                vow +=1
            else:
                cons += 1

        if ((vow == 3) or (cons == 3)):
            seq3 = False

    seq2 = True
    for letter1 in range(len(pw)-1):
        if ((pw[letter1] == pw[letter1+1]) and (pw[letter1] not in 'eo')):
            seq2 = False

    not_state = ""
    if (vow_state and seq3 and seq2):
        not_state = ""
    else:
        not_state = "not "

    print(f"<{pw}> is {not_state}acceptable.")
