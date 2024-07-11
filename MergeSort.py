from utils.DSA import *

def merge(arr, aux, lo, mid, hi):
    aux[lo:hi + 1] = arr[lo:hi + 1]
    i = lo
    j = mid + 1
    for k in range(lo, hi + 1):
        if i > mid:
            arr[k] = aux[j]
            j += 1
        elif j > hi:
            arr[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            arr[k] = aux[j]
            j += 1
        else:
            arr[k] = aux[i]
            i += 1


def sortPart(arr, aux, lo, hi):
    if hi <= lo: return
    mid = (lo + hi) // 2
    sortPart(arr, aux, lo, mid)  # Recursively sorting the left half
    sortPart(arr, aux, mid + 1, hi)  # Recursively sorting the right half
    merge(arr, aux, lo, mid, hi)  # Merging both


def mergeSort(arr):
    n = len(arr)
    aux = [0] * n  # Creates a list/array of 0s of the same size of the original
    sortPart(arr, aux, 0, n - 1)
