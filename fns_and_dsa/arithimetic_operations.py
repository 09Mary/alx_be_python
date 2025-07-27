# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform a basic arithmetic operation on two numbers.

    Parameters:
    - num1: The first number (float).
    - num2: The second number (float).
    - operation: A string specifying the operation ('add', 'subtract', 'multiply', 'divide').

    Returns:
    - The result of the operation, or a specific message if an error occurs (e.g., division by zero).
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
