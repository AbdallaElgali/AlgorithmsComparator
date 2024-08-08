from utils.DSA import *
import random

def merge(a, aux, lo, mid, hi):  # O(N)
    aux[lo:hi+1] = a[lo:hi+1]  # Copy the array
    i = lo
    j = mid + 1

    for k in range(i, hi+1):
        if i > mid:  # The left array is sorted
            a[k] = aux[j]
            j += 1
        elif j > hi:  # The right array is sorted
            a[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:  # Compare element in right array with element in left array
            a[k] = aux[j]
            j += 1
        else:  # If non of the above and aux[i] >= aux[j]
            a[k] = aux[i]
            i += 1

def sortPart(a, aux, lo, hi):  # O(log n)
    if hi<=lo: return
    mid = (lo+hi)//2
    sortPart(a, aux, lo, mid)
    sortPart(a, aux, mid+1, hi)
    merge(a, aux, lo, mid, hi)

def mergeSort(a):
    n = len(a)
    aux = [0]*n
    sortPart(a, aux, 0, n-1)


