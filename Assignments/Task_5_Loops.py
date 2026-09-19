# Task 5.1: Numbers from 1 to 20

print("Numbers from 1 to 20:")

for i in range(1, 21):
    print(i)



# Task 5.2: Multiplication Table

number = int(input("Enter a number: "))

print(f"\nMultiplication Table of {number}")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")



# Task 5.3: Even Numbers using While Loop

number = 2

print("Even numbers from 1 to 50:")

while number <= 50:
    print(number)
    number += 2  