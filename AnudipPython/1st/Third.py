#Write a program to find the largest of 2 numbers.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(f"The largest number is {num1}")
elif num2 > num1:
    print(f"The largest number is {num2}")
else:
    print("Both numbers are equal.")
