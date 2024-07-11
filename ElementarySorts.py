
def insertionSort(arr):
    
    for i in range(len(arr)):
        x = arr[i]  # To be inserted
        j = i - 1
        
        while j >= 0 and x < arr[j]:
             arr[j+1] = arr[j]  # Shift right
             j -= 1
        arr[j+1] = x  # Insert in the correct position
    
    return arr

def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):  # Find the minimum
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Replace the minimum at that position ( 1st min, 2nd min...)
    return arr


def shellSort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr


def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choosing the middle element as the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quickSort(left) + middle + quickSort(right)