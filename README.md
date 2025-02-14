# Uncommon Python Error: ZeroDivisionError Despite Check

This repository demonstrates a subtle error in Python code where a `ZeroDivisionError` can still occur even though a check for a zero divisor is seemingly present. The error arises from the specific order of operations and conditional logic in the code.

## The Bug

The Python function `function_with_uncommon_error` attempts to handle division by zero by checking if `a` is equal to zero. However, the `return b / a` statement is executed before the `else` condition. If `a` is zero, it will still raise a `ZeroDivisionError` before the function's execution reaches the `else` block. This unexpected behavior is due to Python's short-circuiting behavior of `if` statements.

## The Solution

The solution involves restructuring the conditional logic to first check for a zero divisor and return an appropriate value or raise a more specific exception.  The corrected code ensures that the division operation is only attempted if it will not result in a `ZeroDivisionError`.

This example highlights the importance of thorough testing and careful consideration of code execution order, particularly when dealing with potential exceptions.