KM = input().split()
K = int(KM[0])
M = int(KM[1])

arrays = []
for _ in range(K):
    arrays.append([int(x) for x in input().split()][1:])

from itertools import product
possible_combinations = list(product(*arrays))

def modulo(nums):
    return sum(x*x for x in nums) % M

modulii = list(map(modulo,possible_combinations))
result = max(modulii)
print(result)
