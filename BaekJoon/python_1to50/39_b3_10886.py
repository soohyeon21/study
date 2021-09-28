# 10886

# or list 만들어서 count()

n = int(input())

cute = 0
ncute = 0

for _ in range(n):
    vote = int(input())
    if (vote == 0):
        ncute += 1
    else: # (vote == 1)
        cute += 1

if (ncute > cute):
    print("Junhee is not cute!")
else: # (ncute < cute)
    print("Junhee is cute!")
