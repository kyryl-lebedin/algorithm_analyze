import matplotlib
matplotlib.use('Agg')  # Use the non-GUI Agg backend
import matplotlib.pyplot as plt
import numpy as np
import random
import time
import io
import ast
import threading

def get_function_object(code_str):
    function_valid = function_validate(code_str)
    if function_valid != 1:
        return function_valid
    
    local_scope = {}
    
    exec(code_str, globals(), local_scope)
    
    func_name = next(key for key, value in local_scope.items() if callable(value))
    algorithm = local_scope[func_name]
     
    return algorithm



def get_graph(function, input_type):
    
    if input_type == 'list':
            sizes, times = list_input(function)

            plt.figure()
            plt.plot(sizes, times)
            plt.xlabel('Size of List (n)')
            plt.ylabel('Time (s)')
            plt.title('Time Complexity')

            # Save the plot to a BytesIO stream
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            plt.close()  # Close the figure to free memory
            buf.seek(0)  # Rewind your buffer

            #image_base64 = base64.b64encode(buf.getvalue()).decode('ascii')
        

            return buf



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



    

def list_input(function):
    
    n_size = 1000
    a_size = 100
    sizes = list(range(1, n_size)) 
    times = []

   
    for size in sizes:
      
        test_list = [random.randint(1, a_size) for _ in range(size)]

       
        start_time = time.perf_counter()  # Start timing
        function(test_list)  # Execute the function
        end_time = time.perf_counter()  # End timing

        # Calculate the elapsed time and append to times list
        elapsed_time = end_time - start_time
        times.append(elapsed_time)

    # Return the sizes and times
    return sizes, times



# def run_with_timeout(func, args, timeout):
#     result = [None]  # A mutable object to store the function result

#     def target(result, args):
#         result[0] = func(args)

#     thread = threading.Thread(target=target, args=(result, args))
#     thread.start()
#     thread.join(timeout)
#     if thread.is_alive():
#         print("Function timed out")
#         thread.join()  # Optionally wait for thread to actually finish
#     else:
#         return result[0]