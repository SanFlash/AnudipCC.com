primes = [num for num in range(2, 50) if all(num % div != 0 for div in range(2, int(num**0.5) + 1))]
print("Prime numbers less than 50:", primes)
