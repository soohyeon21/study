# 15341

# "4. Sum the results of the previous step, and add to it the sum of all even-labeled digits."
# => step3의 결과에 짝수 항만 더 더하라는 얘기 아니야? 이게 왜 그냥 sum(step3)야??!?! 납득할 수 없어!!
# => ㅎ... 설마 1/2/4만 step이고, 3/5는 각각 2/4의 조건(if)이어서, 4번에서 의미하는 'previous step'이 2번을 말하는 거면 할 말 없다ㅎ

import sys

while (1):
    card = sys.stdin.readline().rstrip().replace(" ", "")
    if (card == '0'*16):
        break

    card = list(map(int, card))
    for i in range(16):
        if (i%2 == 0):
            card[i] *= 2
        if (card[i]> 9):
            card[i] -= 9
            
    step3 = sum(card)
##    for k in range(8):
##        step3 += card[2*k+1]

    if (step3%10 == 0):
        print("Yes")
    else:
        print("No")
