print("Menu:")
print("1. Arithmetic Operators")
print("2. Assignment Operators")
print("3. Bitwise Operators")
print("4. Greatest of Three Numbers")
print("5. Area of Circle")
print("6. Area of Triangle")
print("7. Area of Rectangle")
print("8. Area of Square")
print("9. Exit")

choice = int(input("Enter your choice (1-9): "))

if choice == 1:
    # Arithmetic Operators
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b:.2f}")
    print(f"Modulus: {a} % {b} = {a % b}")

elif choice == 2:
    # Assignment Operators
    a = int(input("Enter the value of a: "))
    print(f"Initial value of a: {a}")
    a += 5
    print(f"After a += 5, a = {a}")
    a -= 3
    print(f"After a -= 3, a = {a}")
    a *= 2
    print(f"After a *= 2, a = {a}")
    a //= 4
    print(f"After a //= 4, a = {a}")
    a %= 3
    print(f"After a %= 3, a = {a}")

elif choice == 3:
    # Bitwise Operators
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(f"Bitwise AND: {a} & {b} = {a & b}")
    print(f"Bitwise OR: {a} | {b} = {a | b}")
    print(f"Bitwise XOR: {a} ^ {b} = {a ^ b}")
    print(f"Bitwise NOT of {a}: ~{a} = {~a}")
    print(f"Left shift {a} by 2: {a} << 2 = {a << 2}")
    print(f"Right shift {a} by 2: {a} >> 2 = {a >> 2}")

elif choice == 4:
    # Greatest of Three Numbers
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))
    if a > b and a > c:
        print(f"The greatest number is {a}")
    elif b > c:
        print(f"The greatest number is {b}")
    else:
        print(f"The greatest number is {c}")

elif choice == 5:
    # Area of Circle
    radius = float(input("Enter the radius of the circle: "))
    pi = 3.14159
    area = pi * radius ** 2
    print(f"The area of the circle is {area:.2f}")

elif choice == 6:
    # Area of Triangle
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is {area:.2f}")

elif choice == 7:
    # Area of Rectangle
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is {area:.2f}")

elif choice == 8:
    # Area of Square
    side = float(input("Enter the side length of the square: "))
    area = side ** 2
    print(f"The area of the square is {area:.2f}")

elif choice == 9:
    # Exit
    print("Exiting the program.")

else:
    print("Invalid choice. Please try again.")
