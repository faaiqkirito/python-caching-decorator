# Python Caching Decorator

A lightweight Python decorator that caches the results of function calls using an internal dictionary.

## Features
- Stores positional and keyword arguments as hashable keys.
- Returns cached results instantly for repeated inputs.
- Preserves function metadata using `functools.wraps`.

## Usage
```python
from caching import cache_results

@cache_results
def multiply(a, b):
    return a * b

print(multiply(4, 5))  # Output: Computed: 20
print(multiply(4, 5))  # Output: From Cache: 20
