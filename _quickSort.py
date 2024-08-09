import random
from utils.DSA import *

def shuffle(a):
    n = len(a)
    for i in range(n):
        r = random.randrange(0, i+1)
        exch(a, i, r)

def partition(a, lo, hi):
    pivot = a[lo]
    i = lo
    j = hi+1

    while True:
        i += 1
        while a[i] < pivot:
            if i == hi:
                break
            i+=1

        j -= 1
        while a[j] > pivot:
            if j == lo:
                break
            j-=1

        if i >= j:
            break
        exch(a, i, j)

    exch(a, j, lo)
    return j

def sort(a, lo, hi):
    if lo>=hi:
        return
    j = partition(a, lo, hi)

    sort(a, lo, j-1)
    sort(a, j+1, hi)

a = [10,54,12,523,6,23,5,26,2,643,5,6,2543,2,5]

print(a)
sort(a, 0, len(a)-1)
print('sorted: ', a)