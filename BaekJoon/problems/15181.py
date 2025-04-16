# 15181

# "the difference between 1 note and the next is 2, 4 or 6 notes 'above' the previous note"

import sys

convert = {'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'A':6, 'B':7}

while (1):
    notes = sys.stdin.readline().rstrip()
    if (notes == "#"):
        break
    
    cnote = [convert[note] for note in notes]
    
    state = True
    for i in range(1, len(notes)):
        diff = cnote[i] - cnote[i-1]
        if (diff < 0):
            diff += 7

        if (diff not in [2, 4, 6]):
            state = False
            break

    if (state):
        print("That music is beautiful.")
    else:
        print("Ouch! That hurts my ears.")
