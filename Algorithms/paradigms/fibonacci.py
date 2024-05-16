"""
    It's an example of using
        Dynamic Programming approach
"""


# Algorithm without optimization
# It cost a lot O(2n)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# After using Dynamic Programming
# It cost a lot O(n)
def optimized_fibonacci(n):
    fib = [0, 1]

    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[n]


# print(fibonacci(500)) very slow.
print(optimized_fibonacci(500))
