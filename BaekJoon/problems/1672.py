# 1672

# python 문자열 slicing의 시간복잡도는 O(k). (단, k=slicing한 문자열 길이)

import sys

table = {'AA':'A', 'AG':'C', 'AC':'A', 'AT':'G',
         'GA':'C', 'GG':'G', 'GC':'T', 'GT':'A',
         'CA':'A', 'CG':'T', 'CC':'C', 'CT':'G',
         'TA':'G', 'TG':'A', 'TC':'G', 'TT':'T'}

n = int(sys.stdin.readline())
dna = sys.stdin.readline().rstrip()[::-1]

end = dna[0]
for i in range(1, n):
    end = table[end+dna[i]]

print(end)
