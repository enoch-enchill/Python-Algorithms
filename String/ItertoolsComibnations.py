"""
This tool returns the R length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.
"""

from itertools import combinations
Sk = input().split()
S = Sk[0]
k = int(Sk[1])
B = ''.join(sorted(S))
for x in range(1, k+1):
    for y in list(combinations(B, x)):
        print(''.join(y))
