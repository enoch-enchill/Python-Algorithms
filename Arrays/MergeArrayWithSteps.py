def makeMagicMix(a,b):
  ab = [] # Joined list
  k = 1 # step
  for i, x in enumerate(a):
    ab.append(x)
    j = i//k
    if i%k == k-1 and j < len(b):
      ab.append(b[j])

  print(ab)


a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
b = ['a', 'b', 'c', 'd', 'e']
makeMagicMix(a,b)
