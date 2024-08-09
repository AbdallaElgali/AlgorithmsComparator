from utils.DSA import *

def heapify(a, n, i):  # O(log n)
    largest = i
    l = 2*i + 1  # left child
    r = 2*i + 2  # right child

    if l < n and a[largest] < a[l]:
        largest = l

    if r < n and a[largest] < a[r]:
        largest = r

    if largest != i:
        exch(a, i, largest)  # swapping the root

        heapify(a, n, largest)

def buildMaxHeap(a):  # O(N)
    for i in range(len(a)//2 - 1, -1, -1):
        heapify(a, i, 0)
def heapSort(a):
    n = len(a)
    buildMaxHeap(a)

    for i in range(n-1, 0, -1):  # O(n-1)
        exch(a, i, 0)
        heapify(a, i, 0)




