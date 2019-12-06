
"""
This tool returns  length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.
"""
from itertools import combinations_with_replacement

Sk = input().split()
S = Sk[0]
k = int(Sk[1])
B = ''.join(sorted(S))
for y in list(combinations_with_replacement(B, k)):
    print(''.join(y))
