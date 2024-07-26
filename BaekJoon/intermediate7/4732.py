# 4732

import sys

scale = [["A"], ["A#", "Bb"], ["B", "Cb"], ["C", "B#"], ["C#", "Db"], ["D"], ["D#", "Eb"], ["E", "Fb"], ["F", "E#"], ["F#", "Gb"], ["G"], ["G#", "Ab"]]

while (1):
    ipt = sys.stdin.readline().rstrip()
    if (ipt == "***"):
        break

    before = ipt.split()
    updown = int(sys.stdin.readline())

    for s in before:
        for j in range(12):
            if (s in scale[j]):
                print(scale[(j+updown+12)%12][0], end=" ")
    print()
