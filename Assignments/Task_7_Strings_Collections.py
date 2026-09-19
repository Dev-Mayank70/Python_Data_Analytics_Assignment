# Task 7: Strings and Collections

# -----------------------------
# 1. String Operations
# -----------------------------

text = "Python Data Analytics"

print("----- String Operations -----")

print("Original String:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Replace:", text.replace("Python", "Advanced Python"))
print("Find 'Data':", text.find("Data"))


# -----------------------------
# 2. List Operations
# -----------------------------

print("\n----- List Operations -----")

fruits = ["Apple", "Banana", "Mango"]

print("Original List:", fruits)

fruits.append("Orange")
print("After append:", fruits)

fruits.remove("Banana")
print("After remove:", fruits)

fruits.sort()
print("After sort:", fruits)


# -----------------------------
# 3. Tuple
# -----------------------------

print("\n----- Tuple -----")

student_tuple = ("Mayank", 21, "BCA")

print("Tuple:", student_tuple)
print("First Element:", student_tuple[0])
print("Second Element:", student_tuple[1])


# -----------------------------
# 4. Dictionary
# -----------------------------

print("\n----- Dictionary -----")

student = {
    "name": "Mayank Gupta",
    "age": 21,
    "branch": "BCA",
    "college": "Future University"
}

print("Student Information:")

for key, value in student.items():
    print(key, ":", value)


# -----------------------------
# 5. Set Operations
# -----------------------------

print("\n----- Set Operations -----")

numbers = {10, 20, 30}

print("Original Set:", numbers)

numbers.add(40)
print("After add:", numbers)

numbers.remove(20)
print("After remove:", numbers)