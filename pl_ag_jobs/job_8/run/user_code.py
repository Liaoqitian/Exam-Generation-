def trib(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n == 2:
        return 4
    return 2 * fib(n - 3) + 3 * fib(n - 2) + 4 * fib(n)