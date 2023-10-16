def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage:
num = int(input(" enter a value :"))
result = factorial_recursive(num)
print(f"The factorial of {num} is {result}")
