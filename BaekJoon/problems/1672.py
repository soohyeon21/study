# 1672

import sys

table = {'AA':'A', 'AG':'C', 'AC':'A', 'AT':'G',
         'GA':'C', 'GG':'G', 'GC':'T', 'GT':'A',
         'CA':'A', 'CG':'T', 'CC':'C', 'CT':'G',
         'TA':'G', 'TG':'A', 'TC':'G', 'TT':'T'}

n = int(sys.stdin.readline())
dna = sys.stdin.readline().rstrip()

for i in range(n-1):
    end = table[dna[-2:]]
    dna = dna[:-2]+end

print(dna)
