# Python Style Guide

This guide covers Python coding standards based on PEP 8 and best practices for writing clean, maintainable code.

## Code Layout

### Indentation
- Use 4 spaces per indentation level
- Never mix tabs and spaces
- Continuation lines should align wrapped elements vertically

### Line Length
- Limit lines to 79 characters maximum
- Use implied line continuation inside parentheses, brackets, and braces
- Prefer parentheses over backslashes for line breaks

### Blank Lines
- Two blank lines around top-level function and class definitions
- One blank line around method definitions inside classes
- Use blank lines sparingly to separate groups of related functions

## Imports
- Import statements should be on separate lines
- Order imports: standard library, related third party, local application
- Use absolute imports when possible
- Group imports with blank lines between different categories

```python
# Correct
import os
import sys

import pandas as pd
import numpy as np

from mypackage import mymodule
```

## Naming Conventions

### Variables and Functions
- Use snake_case for variables and function names
- Use descriptive names that clearly indicate purpose
- Avoid single-letter variables except for short loop counters

### Classes
- Use CapWords (PascalCase) convention for class names
- Keep class names concise but descriptive

### Constants
- Use UPPER_CASE with underscores for constants
- Define constants at module level

### Private Variables
- Use single leading underscore for internal use
- Use double leading underscore for name mangling

## Documentation

### Docstrings
- Use triple double quotes for all docstrings
- Write docstrings for all public modules, functions, classes, and methods
- Keep docstrings concise but informative

```python
def calculate_average(numbers):
    """Calculate the arithmetic mean of a list of numbers.
    
    Args:
        numbers (list): List of numeric values
        
    Returns:
        float: The arithmetic mean
    """
    return sum(numbers) / len(numbers)
```

### Comments
- Write complete sentences with proper capitalization
- Keep comments current and relevant
- Use inline comments sparingly and separate with two spaces

## Programming Best Practices

### Comparisons
- Use `is` and `is not` for comparisons with None, True, False
- Use `not` for boolean negation rather than `== False`
- For sequences, use the fact that empty sequences are falsy

```python
# Correct
if not sequence:
    pass

if value is None:
    pass
```

### Exception Handling
- Be specific about which exceptions to catch
- Use try-except blocks for expected errors only
- Always clean up resources in finally blocks or use context managers

### Function Design
- Keep functions small and focused on a single task
- Use default arguments thoughtfully
- Return consistent types when possible

### Class Design
- Use `__init__` to initialize instance attributes
- Make instance variables private when appropriate
- Use property decorators for computed attributes

## Code Organization

### Module Structure
1. Module docstring
2. Imports
3. Constants
4. Exception classes
5. Other classes
6. Functions
7. Main execution block

### Error Prevention
- Validate inputs at function boundaries
- Use type hints for better code documentation
- Remove unused imports and variables
- Avoid deep nesting - prefer early returns

## Modern Python Features

### Type Hints
- Use type hints for function parameters and return values
- Import types from `typing` module when needed

### Context Managers
- Use `with` statements for file operations and resource management
- Create custom context managers for cleanup operations

### List Comprehensions
- Use list comprehensions for simple transformations
- Avoid complex nested comprehensions - use regular loops instead

This guide promotes code that is readable, maintainable, and follows Python community standards.