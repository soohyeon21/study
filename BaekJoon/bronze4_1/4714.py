# 4714

import sys

while (1):
    earth = float(sys.stdin.readline())
    if (earth < 0):
        break

    moon = earth * 0.167
    print(f"Objects weighing {earth:.2f} on Earth will weigh {moon:.2f} on the moon.")
