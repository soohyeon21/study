# 6841

import sys

trans = {"CU":"see you", ":-)":"I’m happy", ":-(":"I’m unhappy", ";-)":"wink",
         ":-P":"stick out my tongue", "(~.~)":"sleepy","TA":"totally awesome",
         "CCC":"Canadian Computing Competition", "CUZ":"because", "TY":"thank-you",
         "YW":"you’re welcome", "TTYL":"talk to you later"}

while (1):
    ipt = sys.stdin.readline().rstrip()
    if (ipt == ""):
        break

    if (ipt in trans):
        print(trans[ipt])
    else:
        print(ipt)
