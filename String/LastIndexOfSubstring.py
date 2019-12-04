"""
You have been given an array of size N consisting of integers. 
In addition you have been given an element M you need to find and 
print the index of the last occurrence of this element M in the array if it exists in it, 
otherwise print -1. Consider this array to be 1 indexed.
"""

# Write your code here
def findLastIndex(arr, m):
    n = m.split(' ')[1]
    a = list(arr.split(' '))
    if n in a:
        return next(i for i in reversed(range(len(a))) if a[i] == str(n)) +1
        #return ''.join(a).rindex(str(n)) +1
    else:
        return -1
        

m = input()
arr = input()
print(str(findLastIndex(arr, m)))
