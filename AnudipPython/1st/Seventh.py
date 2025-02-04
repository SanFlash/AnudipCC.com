#7. write a menu driven program to calculate the are of different shapes.


print("Menu:")
print("1. Area of Circle")
print("2. Area of Rectangle")
print("3. Area of Triangle")
print("4. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    radius = float(input("Enter the radius of the circle: "))
    pi = 3.14159  # Approximation of π
    area = pi * radius ** 2
    print(f"The area of the circle is {area:.2f}")
elif choice == 2:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is {area:.2f}")
elif choice == 3:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is {area:.2f}")
elif choice == 4:
    print("Exiting the program.")
else:
    print("Invalid choice. Please try again.")
