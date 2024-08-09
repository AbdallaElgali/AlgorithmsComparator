from utils.DSA import *

def _compare(a, b):
    similar = 0
    for i in range(len(a)):
        if a[i] in b:
            similar += 1
    return similar

def get_dups(arr):
    dups = {}
    for i in range(len(arr)):
        if arr[i] in dups.keys():
            dups[arr[i]] += 1
        else:
            dups[arr[i]] = 1
    return dups
def compare(a, b):
    a_b = a + b
    a_dups = get_dups(a)
    a_b_dups = get_dups(a_b)
    similarity = 0
    for key, value in a_b_dups.items():
        if key in a_dups.keys():
            similarity += (value - a_dups[key])
    return similarity

a = [1,6,2,345,23,2423,234,42,3,4,42,34,5234]
b = [3,5,0,2254,324,7,1,4,6,21,2423,2]
print(compare(a,b))

