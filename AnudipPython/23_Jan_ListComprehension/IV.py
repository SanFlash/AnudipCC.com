numbers = [1, 2, 3, 4, 5]
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

factorials = [factorial(num) for num in numbers]

print("Factorials:", factorials)
