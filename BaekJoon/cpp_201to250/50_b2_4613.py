# 4613

# ord("A") # 65
# ord("Z") # 90
# ord(" ") # 32

import sys

while (1):
    packet = sys.stdin.readline().rstrip()
    if (packet == "#"):
        break

    qsum = 0
    for i in range(1, len(packet)+1):
        val = 0
        if (packet[i-1] != " "):
            val = ord(packet[i-1]) - 64
        qsum += i * val
    print(qsum)
