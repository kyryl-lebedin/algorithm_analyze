functions = {
    "constant": 
    {
        "array": [
"""
def constant_function1(arr):
    return 42
""",
"""
def constant_function2(arr):
    return 3.14
""",
"""
def constant_function3(input_array):
    return "constant value"
""",
"""
def constant_function4(input_array):
    return True
""",
"""
def constant_function5(input_array):
    return None
""",
"""
def constant_function6(lst):
    return 0
""",
"""
def constant_function7(sequence):
    x = -1
    return x
""",

"""
def constant_function11(sequence):
    x = -1
    return x
""",
        

        
        ],

        "matrix": [
"""
def constant_function8(matrix):
    return False
""",
"""
def constant_function9(mat):
    return 1
""",
        ],
    
        

    }, 








    "linear": {
        
        "array": [
"""
def linear_function1(arr):
    return sum(arr)
""",
"""
def linear_function2(array_input):
    result = []
    for x in array_input:
        result.append(x * 2)
    return result
""",
"""
def linear_function3(input_array):
    return [item for item in input_array if item > 0]
""",
"""
def linear_function4(data):
    count = 0
    for _ in data:
        count += 1
    return count
""",
"""
def linear_function5(numbers):
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value
""",
"""
def linear_function6(lst):
    squared = [x ** 2 for x in lst]
    return squared
""",
"""
def linear_function7(sequence):
    total = 0
    for i, value in enumerate(sequence):
        total += i * value
    return total
""",
"""
def linear_function16(lst):
    squared = [x ** 2 for x in lst]
    return squared
""",
"""
def linear_function17(sequence):
    total = 0
    for i, value in enumerate(sequence):
        total += i * value
    return total
""",
],



        "matrix": [

"""
def linear_function6(mat):
    for row in mat:
        a = row
""",


        ],
    },

    "polynomial": {

        "array":[

"""
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                # Update the index of the smallest element
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
""",

#

"""
def pairwise_sum(arr):
    sums = []
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            sums.append(arr[i] + arr[j])
    return sums
""",

#

"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
""",
#

"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
""",



"""
def quadratic_function(arr):
    n = len(arr)
    result = []
    # Iterate over all pairs (i, j) where i and j are indices of the array
    for i in range(n):
        for j in range(i, n):
            # Perform some operation with arr[i] and arr[j]
            result.append(arr[i] + arr[j])
    return result
""",

#

"""
def max_product_of_two(arr):
    n = len(arr)
    max_product = float('-inf')

    for i in range(n):
        for j in range(i + 1, n):
            product = arr[i] * arr[j]
            if product > max_product:
                max_product = product

    return max_product

""",


        ],
        
        "matrix": [
"""
def rotate_matrix_90_degrees(matrix):
    n = len(matrix)
    # Create a new matrix to hold the rotated version
    rotated = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = matrix[i][j]
    return rotated
""",

#

"""
def count_nonzero_elements(matrix):
    count = 0
    n = len(matrix)
    for i in range(n):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                count += 1
    return count
""",

#

"""
def sum_of_elements(matrix):
    total = 0
    n = len(matrix)
    for i in range(n):
        for j in range(len(matrix[i])):
            total += matrix[i][j]
    return total
""",

#

"""
def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
""",       
        
        ],


    },
    "log(n)": 
    {   
"array": 
[

"""
def find_max_in_bitonic_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1  # Maximum is in the right half
        else:
            right = mid  # Maximum is in the left half (including mid)

    return arr[left]

""",
#
"""
def find_peak(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1  # Peak is in the right half
        else:
            right = mid  # Peak is in the left half (including mid)

    return arr[left]
""",
#
"""
def find_min_in_rotated_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > arr[right]:
            left = mid + 1  # Minimum is in the right half
        else:
            right = mid  # Minimum is in the left half (including mid)

    return arr[left]
""",
#
"""
def single_non_duplicate(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        # Ensure mid is even
        if mid % 2 == 1:
            mid -= 1

        if arr[mid] == arr[mid + 1]:
            left = mid + 2  # Single element is in the right half
        else:
            right = mid  # Single element is in the left half (including mid)

    return arr[left]
""",
#
"""
def find_fixed_point(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == mid:
            return mid  # Fixed point found at index mid
        elif arr[mid] < mid:
            left = mid + 1  # Fixed point might be in the right half
        else:
            right = mid - 1  # Fixed point might be in the left half

    return -1 
""",
#
"""
def find_peak(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1  # Peak is in the right half
        else:
            right = mid  # Peak is in the left half (including mid)

    return arr[left]
""",
#
"""
def find_peak(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1  # Peak is in the right half
        else:
            right = mid  # Peak is in the left half (including mid)

    return arr[left]
""",
#
"""
def find_min_in_rotated_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > arr[right]:
            left = mid + 1  # Minimum is in the right half
        else:
            right = mid  # Minimum is in the left half (including mid)

    return arr[left]
""",
#
"""
def single_non_duplicate(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        # Ensure mid is even
        if mid % 2 == 1:
            mid -= 1

        if arr[mid] == arr[mid + 1]:
            left = mid + 2  # Single element is in the right half
        else:
            right = mid  # Single element is in the left half (including mid)

    return arr[left]
""",

"""
def find_max_in_bitonic_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1  # Maximum is in the right half
        else:
            right = mid  # Maximum is in the left half (including mid)

    return arr[left]
""",

],

######################
    },
    "nlog(n)": 
    {
"array":
[
"""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    sorted_array = []
    i = j = 0

    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] <= right_sorted[j]:
            sorted_array.append(left_sorted[i])
            i += 1
        else:
            sorted_array.append(right_sorted[j])
            j += 1

    # Append any remaining elements
    sorted_array.extend(left_sorted[i:])
    sorted_array.extend(right_sorted[j:])

    return sorted_array

""",
#
"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: array is already sorted
    
    # Choose a pivot element (using the last element here)
    pivot = arr[-1]
    left = []
    equal = []
    right = []
    
    # Partition the array into three parts
    for x in arr:
        if x < pivot:
            left.append(x)      # Elements less than pivot
        elif x == pivot:
            equal.append(x)     # Elements equal to pivot
        else:
            right.append(x)     # Elements greater than pivot
    
    # Recursively sort the left and right partitions and combine
    return quick_sort(left) + equal + quick_sort(right)

""",
#
"""

def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        # Heapify in place without a helper function
        largest = i
        while True:
            left = 2 * largest + 1
            right = 2 * largest + 2
            new_largest = largest

            if left < n and arr[left] > arr[new_largest]:
                new_largest = left
            if right < n and arr[right] > arr[new_largest]:
                new_largest = right

            if new_largest == largest:
                break

            arr[largest], arr[new_largest] = arr[new_largest], arr[largest]
            largest = new_largest

    # Extract elements one by one
    for i in range(n-1, 0, -1):
        # Move current root to end
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify the reduced heap
        largest = 0
        while True:
            left = 2 * largest + 1
            right = 2 * largest + 2
            new_largest = largest

            if left < i and arr[left] > arr[new_largest]:
                new_largest = left
            if right < i and arr[right] > arr[new_largest]:
                new_largest = right

            if new_largest == largest:
                break

            arr[largest], arr[new_largest] = arr[new_largest], arr[largest]
            largest = new_largest
""",
#
"""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    sorted_array = []
    i = j = 0

    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] <= right_sorted[j]:
            sorted_array.append(left_sorted[i])
            i += 1
        else:
            sorted_array.append(right_sorted[j])
            j += 1

    # Append any remaining elements
    sorted_array.extend(left_sorted[i:])
    sorted_array.extend(right_sorted[j:])

    return sorted_array

""",
#
"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: array is already sorted
    
    # Choose a pivot element (using the last element here)
    pivot = arr[-1]
    left = []
    equal = []
    right = []
    
    # Partition the array into three parts
    for x in arr:
        if x < pivot:
            left.append(x)      # Elements less than pivot
        elif x == pivot:
            equal.append(x)     # Elements equal to pivot
        else:
            right.append(x)     # Elements greater than pivot
    
    # Recursively sort the left and right partitions and combine
    return quick_sort(left) + equal + quick_sort(right)

""",
#
"""

def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        # Heapify in place without a helper function
        largest = i
        while True:
            left = 2 * largest + 1
            right = 2 * largest + 2
            new_largest = largest

            if left < n and arr[left] > arr[new_largest]:
                new_largest = left
            if right < n and arr[right] > arr[new_largest]:
                new_largest = right

            if new_largest == largest:
                break

            arr[largest], arr[new_largest] = arr[new_largest], arr[largest]
            largest = new_largest

    # Extract elements one by one
    for i in range(n-1, 0, -1):
        # Move current root to end
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify the reduced heap
        largest = 0
        while True:
            left = 2 * largest + 1
            right = 2 * largest + 2
            new_largest = largest

            if left < i and arr[left] > arr[new_largest]:
                new_largest = left
            if right < i and arr[right] > arr[new_largest]:
                new_largest = right

            if new_largest == largest:
                break

            arr[largest], arr[new_largest] = arr[new_largest], arr[largest]
            largest = new_largest
""",
"""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    sorted_array = []
    i = j = 0

    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] <= right_sorted[j]:
            sorted_array.append(left_sorted[i])
            i += 1
        else:
            sorted_array.append(right_sorted[j])
            j += 1

    # Append any remaining elements
    sorted_array.extend(left_sorted[i:])
    sorted_array.extend(right_sorted[j:])

    return sorted_array

""",
#
"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: array is already sorted
    
    # Choose a pivot element (using the last element here)
    pivot = arr[-1]
    left = []
    equal = []
    right = []
    
    # Partition the array into three parts
    for x in arr:
        if x < pivot:
            left.append(x)      # Elements less than pivot
        elif x == pivot:
            equal.append(x)     # Elements equal to pivot
        else:
            right.append(x)     # Elements greater than pivot
    
    # Recursively sort the left and right partitions and combine
    return quick_sort(left) + equal + quick_sort(right)

""",
#
"""

def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        # Heapify in place without a helper function
        largest = i
        while True:
            left = 2 * largest + 1
            right = 2 * largest + 2
            new_largest = largest

            if left < n and arr[left] > arr[new_largest]:
                new_largest = left
            if right < n and arr[right] > arr[new_largest]:
                new_largest = right

            if new_largest == largest:
                break

            arr[largest], arr[new_largest] = arr[new_largest], arr[largest]
            largest = new_largest

    # Extract elements one by one
    for i in range(n-1, 0, -1):
        # Move current root to end
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify the reduced heap
        largest = 0
        while True:
            left = 2 * largest + 1
            right = 2 * largest + 2
            new_largest = largest

            if left < i and arr[left] > arr[new_largest]:
                new_largest = left
            if right < i and arr[right] > arr[new_largest]:
                new_largest = right

            if new_largest == largest:
                break

            arr[largest], arr[new_largest] = arr[new_largest], arr[largest]
            largest = new_largest
""",
"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: array is already sorted
    
    # Choose a pivot element (using the last element here)
    pivot = arr[-1]
    left = []
    equal = []
    right = []
    
    # Partition the array into three parts
    for x in arr:
        if x < pivot:
            left.append(x)      # Elements less than pivot
        elif x == pivot:
            equal.append(x)     # Elements equal to pivot
        else:
            right.append(x)     # Elements greater than pivot
    
    # Recursively sort the left and right partitions and combine
    return quick_sort(left) + equal + quick_sort(right)

""",

]

    },
}

