# write a program to accept 5 float values and display its sum and average.


value1 = float(input("Enter the first value: "))
value2 = float(input("Enter the second value: "))
value3 = float(input("Enter the third value: "))
value4 = float(input("Enter the fourth value: "))
value5 = float(input("Enter the fifth value: "))

sum_values = value1 + value2 + value3 + value4 + value5
average = sum_values / 5

print(f"The sum of the values is {sum_values:.2f}")
print(f"The average of the values is {average:.2f}")
