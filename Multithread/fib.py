import functools
# Adding python built in cache to avoid needing to recalculate all the stuff again
@functools.lru_cache(None)

# Due to stack size limit, this function can only handle n < 1200
def fibonacci(number):
    if number > 1:
        return fibonacci(number - 1) + fibonacci(number - 2)
    elif number == 0:
        return 0
    else:
        return 1
# To overcome recursion solution's stack size, will be relying on normal iteration on already calculated values on the heap
def fibonacciNotRecursive(n):
    a, b = 0, 1
    for x in range(0, n):
        a, b = b, a + b
    return a
