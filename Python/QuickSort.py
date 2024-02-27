import random
import matplotlib.pyplot as plt
import numpy as np

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot_index = choose_pivot(arr, low, high)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    ax.clear()
    plt.bar(xaxis, arr)
    plt.pause(0.1)
    return i+1

def choose_pivot(arr, low, high):
    return random.randint(low, high)

arr = [random.randint(1, 1000) for i in range(100)]
xaxis = np.arange(100)

fig, ax = plt.subplots()
ax.bar(xaxis, arr)
plt.pause(0.1)

quick_sort(arr, 0, len(arr) - 1)