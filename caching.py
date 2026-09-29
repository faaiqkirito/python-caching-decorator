import functools

def cache_results(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        
        if key in cache:
            return f"From Cache: {cache[key]}"
        
        result = func(*args, **kwargs)
        cache[key] = result
        return f"Computed: {result}"

    return wrapper


@cache_results
def multiply(a, b):
    return a * b


if __name__ == "__main__":
    print(multiply(4, 5))   # Computed: 20
    print(multiply(4, 5))   # From Cache: 20
    print(multiply(10, 2))  # Computed: 20
