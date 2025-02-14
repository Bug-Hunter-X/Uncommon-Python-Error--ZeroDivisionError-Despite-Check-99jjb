def function_with_uncommon_error_solution(a, b):
    if a == 0:
        if b == 0:
          return 0  # Handle both a and b being zero to avoid division by zero
        else:
          return float('inf') # Or raise a more specific exception: raise ZeroDivisionError("Division by zero")
    else:
        return a / b