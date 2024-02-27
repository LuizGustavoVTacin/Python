import random
import matplotlib.pyplot as plt
import numpy as np

def bubble_sort(arr):
    n = len(arr)
    fig, ax = plt.subplots()
    xaxis = np.arange(n)
    ax.bar(xaxis, arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                ax.clear()
                ax.bar(xaxis, arr)
                plt.pause(0.1) # pause for 0.1 seconds between each iteration

    plt.show()
    return arr

arr = [random.randint(1, 1000) for i in range(100)]
sorted_arr = bubble_sort(arr)
