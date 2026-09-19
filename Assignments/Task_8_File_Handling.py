# Task 8: Basic File Handling

filename = "introduction.txt"

introduction = """
My name is Mayank Gupta.
I am pursuing BCA from Future University.
I am interested in Data Analytics.
I am learning Python, SQL, Excel, and Power BI.
"""

# Writing to the file
with open(filename, "w") as file:
    file.write(introduction)

print("Introduction has been written to the file.")


# Reading from the file
with open(filename, "r") as file:
    content = file.read()

print("\n----- File Contents -----")
print(content)