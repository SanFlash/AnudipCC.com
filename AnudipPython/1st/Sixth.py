# write a program to accept an operator symbol(+,-,*,/,%) and two numbers and perform the arithmetic operations.


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /, %): ")

if operator == '+':
    print(f"The result is: {num1 + num2}")
elif operator == '-':
    print(f"The result is: {num1 - num2}")
elif operator == '*':
    print(f"The result is: {num1 * num2}")
elif operator == '/':
    if num2 != 0:
        print(f"The result is: {num1 / num2}")
    else:
        print("Division by zero is not allowed.")
elif operator == '%':
    if num2 != 0:
        print(f"The result is: {num1 % num2}")
    else:
        print("Modulo by zero is not allowed.")
else:
    print("Invalid operator.")


