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

