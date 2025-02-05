# 1️ Time Class with + Operator Overloading
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __add__(self, other):
        total_minutes = self.minutes + other.minutes
        extra_hours = total_minutes // 60
        final_minutes = total_minutes % 60
        final_hours = self.hours + other.hours + extra_hours
        return Time(final_hours, final_minutes)

    def __str__(self):
        return f"{self.hours} hours, {self.minutes} minutes"

# 2️ Distance Class with * Operator Overloading
class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __mul__(self, scalar):
        total_inches = (self.feet * 12 + self.inches) * scalar
        final_feet = total_inches // 12
        final_inches = total_inches % 12
        return Distance(int(final_feet), int(final_inches))

    def __str__(self):
        return f"{self.feet} feet, {self.inches} inches"

# 3️ Rectangle Class with == Operator Overloading
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __eq__(self, other):
        return self.area() == other.area()

    def __str__(self):
        return f"Rectangle with length {self.length} and width {self.width}"

# 🎯 Testing the Classes

# Testing Time Class
time1 = Time(2, 45)
time2 = Time(1, 30)
total_time = time1 + time2
print("Total Time:", total_time)

# Testing Distance Class
distance1 = Distance(5, 8)
scaled_distance = distance1 * 3
print("Scaled Distance:", scaled_distance)

# Testing Rectangle Class
rectangle1 = Rectangle(4, 5)  # Area = 20
rectangle2 = Rectangle(2, 10)  # Area = 20
if rectangle1 == rectangle2:
    print("Both rectangles have the same area.")
else:
    print("Rectangles have different areas.")
