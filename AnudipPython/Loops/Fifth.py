rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")  # Adding spaces for alignment
    print("*" * (2 * i - 1))  # Printing stars
