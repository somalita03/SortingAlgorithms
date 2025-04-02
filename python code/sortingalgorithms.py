import time

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main":
    input_data = [64, 34, 25, 12, 22, 11, 90]

    # Bubble Sort
    bubble_sort_data = input_data.copy()
    start_time = time.time()
    bubble_sort(bubble_sort_data)
    end_time = time.time()
    print("Bubble Sort Sorted Array:", bubble_sort_data)
    print("Bubble Sort Runtime: {:.6f} seconds".format(end_time - start_time))

    # Selection Sort
    selection_sort_data = input_data.copy()
    start_time = time.time()
    selection_sort(selection_sort_data)
    end_time = time.time()
    print("Selection Sort Sorted Array:", selection_sort_data)
    print("Selection Sort Runtime: {:.6f} seconds".format(end_time - start_time))

    # Insertion Sort
    insertion_sort_data = input_data.copy()
    start_time = time.time()
    insertion_sort(insertion_sort_data)
    end_time = time.time()
    print("Insertion Sort Sorted Array:", insertion_sort_data)
    print("Insertion Sort Runtime: {:.6f} seconds".format(end_time - start_time))

    # Merge Sort
    merge_sort_data = input_data.copy()
    start_time = time.time()
    merge_sort(merge_sort_data)
    end_time = time.time()
    print("Merge Sort Sorted Array:", merge_sort_data)
    print("Merge Sort Runtime: {:.6f} seconds".format(end_time - start_time))

    # Quick Sort
    quick_sort_data = input_data.copy()
    start_time = time.time()
    quick_sort_data = quick_sort(quick_sort_data)
    end_time = time.time()
    print("Quick Sort Sorted Array:", quick_sort_data)
    print("Quick Sort Runtime: {:.6f} seconds".format(end_time - start_time))


import time

# Heap Sort
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

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

# Counting Sort
def counting_sort(arr):
    max_value = max(arr)
    min_value = min(arr)
    range_of_elements = max_value - min_value + 1

    count_array = [0] * range_of_elements
    output_array = [0] * len(arr)

    for i in range(len(arr)):
        count_array[arr[i] - min_value] += 1

    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output_array[count_array[arr[i] - min_value] - 1] = arr[i]
        count_array[arr[i] - min_value] -= 1

    for i in range(len(arr)):
        arr[i] = output_array[i]

# Radix Sort
def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp)
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_value = max(arr)
    exp = 1
    while max_value // exp > 0:
        counting_sort_radix(arr, exp)
        exp *= 10

# Bucket Sort
def bucket_sort(arr):
    max_value = max(arr)
    min_value = min(arr)
    range_of_elements = max_value - min_value + 1

    bucket_size = 10
    buckets = [[] for _ in range(bucket_size)]

    for num in arr:
        index = (num - min_value) * bucket_size // range_of_elements
        buckets[index].append(num)

    sorted_array = []
    for bucket in buckets:
        if len(bucket) > 0:
            bucket.sort()
            sorted_array.extend(bucket)

    return sorted_array

# Shell Sort
def shell_sort(arr):
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

if __name__ == "__main__":
    input_data = [64, 34, 25, 12, 22, 11, 90]

    # Heap Sort
    heap_sort_data = input_data.copy()
    start_time = time.time()
    heap_sort(heap_sort_data)
    end_time = time.time()
    print("Heap Sort Sorted Array:", heap_sort_data)
    print("Heap Sort Runtime: {:.6f} seconds".format(end_time - start_time))

    # Counting Sort
    counting_sort_data = input_data.copy()
    start_time = time.time()
    counting_sort(counting_sort_data)
    end_time = time.time()
    print("Counting Sort Sorted Array:", counting_sort_data)
    print("Counting Sort Runtime: {:.6f} seconds".format(end_time - start_time))

    # Radix Sort
    radix_sort_data = input_data.copy()
    start_time = time.time()
    radix_sort(radix_sort_data)
    end_time = time.time()
    print("Radix Sort Sorted Array:", radix_sort_data)
    print("Radix Sort Runtime: {:.6f} seconds".format(end_time - start_time))

    # Bucket Sort
    bucket_sort_data = input_data.copy()
    start_time = time.time()
    sorted_data = bucket_sort(bucket_sort_data)
    end_time = time.time()
    print("Bucket Sort Sorted Array:", sorted_data)
    print("Bucket Sort Runtime: {:.6f} seconds".format(end_time - start_time))

    # Shell Sort
    shell_sort_data = input_data.copy()
    start_time = time.time()
    shell_sort(shell_sort_data)
    end_time = time.time()
    print("Shell Sort Sorted Array:", shell_sort_data)
    print("")



import time

# Heap Sort
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

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

# Counting Sort
def counting_sort(arr):
    max_value = max(arr)
    min_value = min(arr)
    range_of_elements = max_value - min_value + 1

    count_array = [0] * range_of_elements
    output_array = [0] * len(arr)

    for i in range(len(arr)):
        count_array[arr[i] - min_value] += 1

    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output_array[count_array[arr[i] - min_value] - 1] = arr[i]
        count_array[arr[i] - min_value] -= 1

    for i in range(len(arr)):
        arr[i] = output_array[i]

# Radix Sort
def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp)
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_value = max(arr)
    exp = 1
    while max_value // exp > 0:
        counting_sort_radix(arr, exp)
        exp *= 10

# Bucket Sort
def bucket_sort(arr):
    max_value = max(arr)
    min_value = min(arr)
    range_of_elements = max_value - min_value + 1

    bucket_size = 10
    buckets = [[] for _ in range(bucket_size)]

    for num in arr:
        index = (num - min_value) * bucket_size // range_of_elements
        buckets[index].append(num)

    sorted_array = []
    for bucket in buckets:
        if len(bucket) > 0:
            bucket.sort()
            sorted_array.extend(bucket)

    return sorted_array

# Shell Sort
def shell_sort(arr):
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

if __name__ == "__main__":
    input_data = [64, 34, 25, 12, 22, 11, 90]

    # Heap Sort
    heap_sort_data = input_data.copy()
    start_time = time.time()
    heap_sort(heap_sort_data)
    end_time = time.time()
    print("Heap Sort Sorted Array:", heap_sort_data)
    print("Heap Sort Runtime: {:.6f} seconds".format(end_time - start_time))

    # Counting Sort
    counting_sort_data = input_data.copy()
    start_time = time.time()
    counting_sort(counting_sort_data)
    end_time = time.time()
    print("Counting Sort Sorted Array:", counting_sort_data)
    print("Counting Sort Runtime: {:.6f} seconds".format(end_time - start_time))

    # Radix Sort
    radix_sort_data = input_data.copy()
    start_time = time.time()
    radix_sort(radix_sort_data)
    end_time = time.time()
    print("Radix Sort Sorted Array:", radix_sort_data)
    print("Radix Sort Runtime: {:.6f} seconds".format(end_time - start_time))

    # Bucket Sort
    bucket_sort_data = input_data.copy()
    start_time = time.time()
    sorted_data = bucket_sort(bucket_sort_data)
    end_time = time.time()
    print("Bucket Sort Sorted Array:", sorted_data)
    print("Bucket Sort Runtime: {:.6f} seconds".format(end_time - start_time))

    # Shell Sort
    shell_sort_data = input_data.copy()
    start_time = time.time()
    shell_sort(shell_sort_data)
    end_time = time.time()
    print("Shell Sort Sorted Array:", shell_sort_data)
    print("")



import time
import random

# Cycle Sort
def cycle_sort(arr):
    n = len(arr)
    for i in range(n):
        while i != arr[i]:
            val = arr[i]
            arr[i]=arr[val]
            arr[val]=val

# Bead Sort (not practical)
def bead_sort(arr):
    def bead_ones(row):
        ones = 0
        for i in range(len(row)):
            if row[i] == '1':
                ones += 1
            else:
                break
        return ones

    for _ in range(len(arr)):
        for i in range(len(arr)):
            ones = bead_ones(arr[i])
            if ones > 0:
                for j in range(ones):
                    if i + j >= len(arr):
                        arr.append("0")
                    arr[i + j] = "0"
                for j in range(ones, len(arr) - i):
                    if i + j >= len(arr):
                        arr.append("1")
                    arr[i + j] = "1"

# Comb Sort
def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink_factor = 1.3
    swapped = True

    while gap > 1 or swapped:
        gap = max(1, int(gap / shrink_factor))
        swapped = False

        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True

# Pancake Sort
def flip(arr, k):
    i = 0
    while i < k / 2:
        arr[i], arr[k - i - 1] = arr[k - i - 1], arr[i]
        i += 1

def pancake_sort(arr):
    n = len(arr)
    for curr_size in range(n, 1, -1):
        max_index = arr.index(max(arr[:curr_size]))
        if max_index != curr_size - 1:
            if max_index != 0:
                flip(arr, max_index + 1)
            flip(arr, curr_size)

# Block Sort (not widely used)
def block_sort(arr):
    block_size = int(len(arr) ** 0.5)
    min_value, max_value = min(arr), max(arr)
    bucket_range = (max_value - min_value + 1) // block_size + 1
    buckets = [[] for _ in range(bucket_range)]
    for value in arr:
        index = (value - min_value) // block_size
        buckets[index].append(value)
    arr = [value for bucket in buckets for value in sorted(bucket)]
    return arr

if __name__ == "__main__":
    input_data = [64, 34, 25, 12, 22, 11, 90]

    # Bead Sort (not practical)
    bead_sort_data = [random.randint(0, 1) for _ in range(50)]
    start_time = time.time()
    bead_sort(bead_sort_data)
    end_time = time.time()
    print("Bead Sort Sorted Array:", bead_sort_data)
    print("Bead Sort Runtime: {:.6f} seconds".format(end_time - start_time))

    # Comb Sort
    comb_sort_data = input_data.copy()
    start_time = time.time()
    comb_sort(comb_sort_data)
    end_time = time.time()
    print("Comb Sort Sorted Array:", comb_sort_data)
    print("Comb Sort Runtime: {:.6f} seconds".format(end_time - start_time))

    # Pancake Sort
    pancake_sort_data = input_data.copy()
    start_time = time.time()
    pancake_sort(pancake_sort_data)
    end_time = time.time()
    print("Pancake Sort Sorted Array:", pancake_sort_data)
    print("Pancake Sort Runtime: {:.6f} seconds".format(end_time - start_time))

    # Block Sort (not widely used)
    block_sort_data = input_data.copy()
    start_time = time.time()
    block_sort_data = block_sort(block_sort_data)
    end_time = time.time()
    print("Block Sort Sorted Array:", block_sort_data)
    print("Block Sort Runtime: {:.6f} seconds".format(end_time - start_time))
        # Cycle Sort
    cycle_sort_data = input_data.copy()
    start_time = time.time()
    cycle_sort(cycle_sort_data)
    end_time = time.time()
    print("Cycle Sort Sorted Array:", cycle_sort_data)
    print("Cycle Sort Runtime: {:.6f} seconds".format(end_time - start_time))