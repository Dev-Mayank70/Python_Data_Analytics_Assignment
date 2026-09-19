# Task 6: User-Defined Functions

def calculate_square(number):
    return number ** 2


def calculate_average(num1, num2, num3):
    return (num1 + num2 + num3) / 3


number = float(input("Enter a number to calculate square: "))

a = float(input("Enter first number for average: "))
b = float(input("Enter second number for average: "))
c = float(input("Enter third number for average: "))

square = calculate_square(number)
average = calculate_average(a, b, c)

print("\n----- Results -----")
print("Square:", square)
print("Average:", average)