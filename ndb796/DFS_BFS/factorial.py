def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

def factorial2(n):
    if n == 1:
        return 1
    return n * factorial2(n - 1)

print(factorial2(5))