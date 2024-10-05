import matplotlib
matplotlib.use('Agg')  # Use the non-GUI Agg backend
import matplotlib.pyplot as plt
import numpy as np
import random
import time
import io
import ast
import threading
import string
import joblib   


def get_function_object(code_str):
    function_valid = function_validate(code_str)
    if function_valid != 1:
        return function_valid
    local_scope = {}
    # Execute the function definon in a scope where it can recursively reference itself
    exec(code_str, local_scope, local_scope)  # Using local_scope as both global and local scope
    func_name = next(key for key, value in local_scope.items() if callable(value))
    algorithm = local_scope[func_name]
    
    return algorithm





def function_validate(code_str):
    try:
        
        tree = ast.parse(code_str)
    except SyntaxError:
        return "Invalid Python code."

    
    has_function = False
    for node in ast.walk(tree):
        # Check for import statements
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            return "Invalid code: Import statements are not allowed."

        # Check for calls to harmful functions
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in {'exec', 'eval', 'open', 'input', '__import__', 'getattr',  'setattr', 'delattr', 'globals', 
                                                                    'locals', '__subclasses__', '__bases__', '__subclasshook__', '__init_subclass__', '__class__', 'memoryview'}:
                return "Invalid code: Usage of {'exec', 'eval', 'open', 'input', '__import__', 'getattr',  'setattr', 'delattr', 'globals', 'locals', '__subclasses__', '__bases__', '__subclasshook__', '__init_subclass__', '__class__', 'memoryview'} is not allowed."

        # Check for exactly one function at the top level
        if isinstance(node, ast.FunctionDef):
            if has_function:
                return "Invalid code: More than one function definition detected."
            has_function = True

    if has_function:
        return 1
    else:
        return "Invalid code: No function definition detected."



run = True



def algorithm_analyze(func, input_type, n, a):
    
    pol_degree = 3

    



    def get_graph(function, input_type):
        
    

        if input_type == 'array':
            sizes, test_input = array_input()

        if input_type == 'array & random index':
            sizes, test_input = array_index_input()
            
        if input_type == 'nxn matrix':
            sizes, test_input = matrix_input()
            

        # if input_type == 'string with letters only':
        #     sizes, test_input = letter_string_input()

        # if input_type == 'string':
        #     sizes, test_input = all_string_input()

        if input_type == 'simple graph (adjacency matrix)':
            sizes, test_input = graph_matrix_input()
        
        
        
        times = measure_times(function, test_input)
        
            # Fit a polynomial curve to the data
        coefficients = np.polyfit(sizes, times, deg=pol_degree)  # Degree 4 polynomial
        poly = np.poly1d(coefficients)

        # Generate smooth data for the fitted curve
        smooth_sizes = np.linspace(min(sizes), max(sizes), 500)  # Smooth sizes from min to max size
        smooth_times = poly(smooth_sizes)  # Evaluate polynomial

        plt.figure()
        plt.plot(sizes, times, 'o', markersize=3, label='Original Data')  # Original data points
        plt.plot(smooth_sizes, smooth_times, 'r-', label='Fitted Curve')  # Fitted curve
        plt.xlabel('Size of List (n)')
        plt.ylabel('Time (s)')
        plt.title('Time Complexity')
        plt.legend()

        # Save the plot to a BytesIO stream
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close()  # Close the figure to free memory
        buf.seek(0)  # Rewind your buffer

        return buf, coefficients.tolist()  # Return the buffer and coefficients as a list
    


    def array_input(n_size=n, a_size=a):
        sizes = list(range(1, n_size))
        test_lists = []

        for size in sizes:
            test_list = [random.randint(0, a_size) for _ in range(size)]
            test_lists.append(test_list)

        return sizes, test_lists
    
    def array_index_input(n_size=n, a_size=a):
        sizes = list(range(1, n_size))
        test_lists_indexes_pairs = []
        

        for size in sizes:
            test_list = [random.randint(0, a_size) for _ in range(size)]
            random_index = random.randint(0, size-1)
            pair = [test_list, random_index]
            test_lists_indexes_pairs.append(pair)
            
 

        
        
        return sizes, test_lists_indexes_pairs
    
    def matrix_input(n_size=n, a_size=a):
        sizes = list(range(1, n_size))
        test_matrices = []

        for size in sizes:
            test_matrix = [[random.randint(0, a_size) for _ in range(size)] for _ in range(size)]
            test_matrices.append(test_matrix)
        
        return sizes, test_matrices
    
    def graph_matrix_input(n_size=n, a_size=a):
        sizes = list(range(1, n_size))
        test_matrices = []

        for size in sizes:
            test_matrix = [[random.randint(0, a_size) for _ in range(size)] for _ in range(size)]
            test_matrices.append(test_matrix)
        
        return sizes, test_matrices
    
    # def letter_string_input(n_size=5000):
    #     sizes = list(range(1, n_size))
    #     test_strings = []

    #     for size in sizes:
    #         test_string = ''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(size)])
    #         test_strings.append(test_string)
        
    #     return sizes, test_strings
    
    # def all_string_input(n_size=5000):
    #     char_pool = string.ascii_letters + string.digits + string.punctuation
    #     sizes = list(range(1, n_size))
    #     test_strings = []

    #     for size in sizes:
    #         test_string = ''.join(random.choice(char_pool) for _ in range(size))
    #         test_strings.append(test_string)

    #     return sizes, test_strings

    



    def print_i(stop_event):
        while not stop_event.is_set():
            print('i')
            time.sleep(2)

    def measure_times(function, test_input):
        global run

        # Create a stop event for the printer thread
        stop_event = threading.Event()
        
        # Start the parallel thread for printing 'i'
        printer_thread = threading.Thread(target=print_i, args=(stop_event,), daemon=True)
        printer_thread.start()

        times = []
        start = time.time()
        for test_list in test_input:
            elapsed_time = time.time() - start
            if elapsed_time > 60:
                print("Time limit exceeded.")
                break
            
            start_time = time.perf_counter()
            if input_type == 'array & random index':
                function(*test_list)
            else:
                function(test_list)
            end_time = time.perf_counter()

            elapsed_time = end_time - start_time
            times.append(elapsed_time)

        # Signal the printer thread to stop
        stop_event.set()

        # Wait for the printer thread to finish
        printer_thread.join()
        print('done')
        return times


    
    cls_sign = ['O(1)', 'O(n)', 'O(log(n))', 'O(nlog(n))', 'O(n<sup>a</sup>)']
    classes = ['constant', 'linear', 'logarithmic', 'log linear', 'polynomial']
    def model_prediction(coefficients):
        loaded_model = joblib.load('model/random_forest_model.pkl')
        label_encoder = joblib.load('model/label_encoder.pkl')
        scaler = joblib.load('model/scaler.pkl')
        data_normalized = scaler.transform([coefficients])
    
        predicted_probabilities = loaded_model.predict_proba(data_normalized)[0]
        
        sorted_predictions = sorted(
        [(class_name, prob) for class_name, prob in zip(classes, predicted_probabilities) if prob > 0], 
        key=lambda x: x[1], 
        reverse=True
        )
    
    # Convert to a dictionary and ensure probabilities are Python floats
        prediction_dict = {class_name: float(prob) for class_name, prob in sorted_predictions}
       
        print(loaded_model.predict(data_normalized))
        class_sign = cls_sign[loaded_model.predict(data_normalized)[0]]
       
        return prediction_dict, class_sign
    
    

    buf, coefficients = get_graph(func, input_type)
    
    predictions, cls_sign = model_prediction(coefficients)
    print(cls_sign)
    
    return buf, predictions, cls_sign


input_types = {'array': ['Array size', 700, 500, 699, 499], 
               'array & random index': ['Array size', 700, 500, 699, 499], 
               'nxn matrix': ['Matrix size', 500, 200, 499, 199], 
               'simple graph (adjacency matrix)': ['Number of vertices', 500, 1, 499, 1]}



algorithm_types = { 
        'Custom': {
        'input_type': 'Custom',
        'algorithms': [],
        'template':
"""def your_custom_algorithm(  ):
    # Type your your code here :)
"""
    },

    'Sorting': {
        'input_type': 'array',
        'algorithms': ['bubble sort', 'selection sort', 'quick sort', 'merge sort'],
        'template':
"""def your_sorting_algorithm(arr):
    # Type your your code here, or select algorithm example :)
"""
    },

    'Searching': {
        'input_type': 'array & random index',
        'algorithms': ['linear search', 'binary search'],
        'template':
"""def your_searching_algorithm(arr, x):
    # Type your your code here, or select algorithm example :)
"""
    },

    'Selecting': {
        'input_type': 'array & random index',
        'algorithms': ['quick select', 'median of medians'],
        'template':
"""def your_selecting_algorithm(arr, k):
    # Type your your code here, or select algorithm example :)
"""
    },

    'Matrix': {
        'input_type': 'nxn matrix',
        'algorithms': ['matrix transpose', 'frobenius norm'],
        'template':
"""def your_matrix_algorithm(matrix):
    # Type your your code here, or select algorithm example :)
"""
    },

#     'Graph': {
#         'input_type': 'simple graph (adjacency matrix)',
#         'algorithms': ['depth first search', 'breadth first search', 'dijkstra'],
#         'template':
# """def your_graph_algorithm(graph, start):
#     # Type your your code here, or select algorithm example :)
# """
#    },



}

algorithms = {
    'bubble sort': """def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
        """, 
        
    'selection sort': """def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
        """,

    'quick sort': """def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
        """,

    'merge sort': """def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
""",

    'linear search': """def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
        """,

    'binary search': """def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1
        """,

    'quick select': """def quick_select(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = arr[len(arr) // 2]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if k < len(left):
        return quick_select(left, k)
    elif k < len(left) + len(middle):
        return middle[0]
    else:
        return quick_select(right, k - len(left) - len(middle))

""",
    'median of medians': """def median_of_medians(arr, k):
    if len(arr) <= 5:
        arr.sort()
        return arr[k]

    # Divide the array into chunks of 5 and find the medians of each chunk
    medians = [median_of_medians(arr[i:i+5], len(arr[i:i+5]) // 2) for i in range(0, len(arr), 5)]
    
    # Find the median of the medians
    pivot = median_of_medians(medians, len(medians) // 2)
    
    # Partition the array into three parts: less than, equal to, and greater than pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    if k < len(left):
        return median_of_medians(left, k)
    elif k < len(left) + len(middle):
        return pivot
    else:
        return median_of_medians(right, k - len(left) - len(middle))

        """,

    'matrix transpose': """def matrix_transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix
        """,

    'frobenius norm': """def frobenius_norm(matrix):
    return sum(sum(x**2 for x in row) for row in matrix) ** 0.5
        """,

    # 'depth first search': """def dfs(graph, start):
    # visited = set()
    # stack = [start]
    # while stack:
    #     vertex = stack.pop()
    #     if vertex not in visited:
    #         visited.add(vertex)
    #         stack.extend(graph[vertex] - visited)
    # return visited
    #     """,

    # 'breadth first search': """def bfs(graph):
    # visited = set()
    # queue = [0]  # Assuming the BFS starts from node 0
    # while queue:
    #     vertex = queue.pop(0)
    #     if vertex not in visited:
    #         visited.add(vertex)
    #         # Extend the queue with all neighbors of vertex that have not been visited
    #         for neighbor, is_connected in enumerate(graph[vertex]):
    #             if is_connected == 1 and neighbor not in visited:
    #                 queue.append(neighbor)
    # return visited
    #     """,

    'dijkstra': """def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            new_distance = distances[vertex] + graph[vertex][neighbor]
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                queue.append(neighbor)
    return distances
""",
}
