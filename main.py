from utils.DSA import *
import random
from MergeSort import mergeSort
from ElementarySorts import insertionSort, shellSort, selectionSort, quickSort
import matplotlib.pyplot as plt

def generate_test_data(arr):
    for i in range(len(arr)):
        arr[i] = random.randint(0, 1000)
    return arr

def measure_time(sort_func, data):
    start_time = time.time()
    sort_func(data)
    end_time = time.time()
    return end_time - start_time


def compare_sorting_algorithms():
    sizes = [10, 100, 1000, 10000, 100000]
    algorithms = {
        'Selection Sort': selectionSort,
        'Insertion Sort': insertionSort,
        'Merge Sort': mergeSort,
        'Quick Sort': quickSort,
        'Shell Sort': shellSort,
        'Python sorted': sorted
    }

    results = {alg: [] for alg in algorithms}

    for size in sizes:
        data = intArray(size)
        generate_test_data(data)
        print(f"Sorting list of size {size}")

        for name, func in algorithms.items():
            time_taken = measure_time(func, data)
            results[name].append(time_taken)
            print(f"{name}: {time_taken:.6f} seconds")

    return sizes, results

def visualize_results(sizes, results):
    for alg, times in results.items():
        plt.plot(sizes, times, label=alg)

    plt.xlabel('List Size')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.title('Sorting Algorithm Performance')
    plt.show()

if __name__ == '__main__':
    sizes, results = compare_sorting_algorithms()
    visualize_results(sizes, results)
