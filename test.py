def get_function_object(code_str):
    """
    This function takes a string of Python code defining a function and returns the function object.

    Args:
    code_str (str): A string containing a valid Python function definition.

    Returns:
    function: The Python function object defined in the input string.
    """
    # Define a dictionary to hold the local scope after exec
    local_scope = {}
    
    # Execute the function definition in code_str within the local scope
    exec(code_str, globals(), local_scope)
    
    # Extract the function object from local_scope
    # Assuming the function name can be extracted as the first 'def' occurrence
    func_name = next(key for key, value in local_scope.items() if callable(value))
    return local_scope[func_name]

# Example usage
code_string = """
def my_function(x):
    print("hello")
    return x * 2
"""
function_object = get_function_object(code_string)
print(function_object(10))  # Output will be 20

def bubble_sort(arr):
            n = len(arr)
            for i in range(n):
                for j in range(0, n-i-1):
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
            return arr

print(bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])) 

def selection_sort(arr):
            n = len(arr)
            for i in range(n):
                min_idx = i
                for j in range(i+1, n):
                    if arr[j] < arr[min_idx]:
                        min_idx = j
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
            return arr

print(selection_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))