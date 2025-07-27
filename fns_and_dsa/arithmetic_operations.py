# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation on two numbers.

    Parameters:
    - num1: First number
    - num2: Second number
    - operation: 'add', 'subtract', 'multiply', or 'divide'

    Returns:
    - Result of the operation or error message if invalid
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
