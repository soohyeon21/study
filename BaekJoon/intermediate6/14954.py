# 14954

# If n is not a happy number, it has been proved by mathematicians
# that repeatedly applying function f to n reaches the following cycle:
# 4 - 16 - 37 - 58 - 89 - 145 - 42 - 20 - 4
# => "UNHAPPY"인 n은 위의 cycle을 포함한다는 얘기일까?
#    그런데 n=5일때는 5-25-29-85-189-146-53-34-25 이던데...

import sys

n = int(sys.stdin.readline())
results = []

fn = n
state = ""
while (1):
    fn = sum(int(x)**2 for x in str(fn))
    if (fn == 1):
        state = "HAPPY"
        break
    if (fn in results):
        state = "UNHAPPY"
        break
    results.append(fn)

print(state)
