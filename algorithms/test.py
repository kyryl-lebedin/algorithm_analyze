def recursive_sum(arr):
    # Base case: if the array is empty, return 0
    if not arr:
        return 0
    # Recursive case: sum the first element with the sum of the rest of the array
    else:
        return arr[0] + recursive_sum(arr[1:])
    

array = [i for i in range(1, 1001)]

print(array)
print(recursive_sum(array))
