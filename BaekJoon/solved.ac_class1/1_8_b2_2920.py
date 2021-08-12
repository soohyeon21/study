# 2920

# or else
# asc 대신 sorted(리스트)
# desc 대신 sorted(리스트, reverse = True)

n = list(map(int, input().split()))

asc = [1, 2, 3, 4, 5, 6, 7, 8]
desc = [8, 7, 6, 5, 4, 3, 2, 1]

if (n == asc):
    print("ascending")
elif (n == desc):
    print("descending")
else:
    print("mixed")
