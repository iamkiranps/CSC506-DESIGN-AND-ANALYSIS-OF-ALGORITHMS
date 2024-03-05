
"""
  Kiran Ponappan Sreekumari 
  CSC506 – Design and Analysis of Algorithms 
  Colorado State University - Global
  Dr. Dong Nguyen 
  March 4, 2024
  Module 8: Discussion Forum
  A bubble sort can be modified to "bubble" in both directions. The first pass moves "up" the list, and the second pass moves "down." 
  This alternating pattern continues until no more passes are necessary. Implement this variation and describe under what circumstances it might be appropriate.
"""
import random
import timeit
import pandas as pd
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def modified_bubble_sort(arr):
    n = len(arr)
    sorted_flag = True  # Flag to track if any swaps occurred

    while sorted_flag:
        sorted_flag = False

        # Move "up" the list
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted_flag = True

        # If no swaps occurred during the "up" pass, break the loop
        if not sorted_flag:
            break

        sorted_flag = False

        # Move "down" the list
        for i in range(n - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                sorted_flag = True
    return arr

def selection_sort(arr):
    n = len(arr)

    # Traverse through all elements in the array
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

# Example usage:
if __name__ == "__main__":

    performance_list = []
    cols = ["Range","Bubble Sort (Pre Sorted)", "Modified Bubble Sort (Pre Sorted)", "Bubble Sort", "Modified Bubble Sort", "Selection Sort",\
            "Insertion Sort", "Merge Sort", "Quick Sort", "Heap Sort"]
    for i in range(1,1000,10):
        random_list = [random.randint(1, i) for _ in range(i)]
        # print(random_list)
        sbs_time_taken = timeit.timeit(lambda: bubble_sort(sorted(random_list.copy())) , number=1)
        smbs_time_taken = timeit.timeit(lambda: modified_bubble_sort(sorted(random_list.copy())) , number=1)
        bs_time_taken = timeit.timeit(lambda: bubble_sort(random_list.copy()) , number=1)
        mbs_time_taken = timeit.timeit(lambda: modified_bubble_sort(random_list.copy()) , number=1)

        ss_time_taken = timeit.timeit(lambda: selection_sort(random_list.copy()) , number=1)
        is_time_taken = timeit.timeit(lambda: insertion_sort(random_list.copy()) , number=1)
        ms_time_taken = timeit.timeit(lambda: merge_sort(random_list.copy()) , number=1)
        qs_time_taken = timeit.timeit(lambda: quick_sort(random_list.copy(), i, i) , number=1)
        hs_time_taken = timeit.timeit(lambda: heap_sort(random_list.copy()) , number=1)
        
        performance_list.append([i,sbs_time_taken,smbs_time_taken,bs_time_taken,mbs_time_taken, ss_time_taken, is_time_taken,\
                                 ms_time_taken, qs_time_taken, hs_time_taken])
    
    # print(performance_list)

    df = pd.DataFrame(performance_list, columns = cols)
    x = df['Range']
    fig, ax1 = plt.subplots(1,1, figsize=(15,5))
    fig.suptitle("Performance Comparison")
    ax1.plot(x, df[[cols[1], cols[2], cols[3], cols[4]]])
    # ax1.loglog()  # Log scale for x-axis
    ax1.legend([cols[1],cols[2], cols[3], cols[4]], loc = "upper left")
    ax1.set_xlabel("Input Size (n)")
    ax1.set_ylabel("Time Complexity")
    
    plt.show()