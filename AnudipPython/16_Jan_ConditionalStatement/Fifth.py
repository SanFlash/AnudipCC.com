#Write a Python program that determines the largest of three numbers entered by the user using nested if syntax.


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 > num2:
    if num1 > num3:
        print(f"The largest number is {num1}")
    else:
        print(f"The largest number is {num3}")
else:
    if num2 > num3:
        print(f"The largest number is {num2}")
    else:
        print(f"The largest number is {num3}")
