# 2455

people = 0
greatest = 0
for _ in range(4):
    out, inn = map(int, input().split())
    people -= out
    people += inn
    greatest = max(people, greatest)

print(greatest)
