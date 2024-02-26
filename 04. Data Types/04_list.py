#------------Creating List------
print("Creating List")
# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]
print(numbers)

# Creating a list of strings
program = ["Python", "Java", "JavaScript"]
print(program)

# Creating a list with mixed data types
mixed_list = [1, "apple", True, 3.14]
print(mixed_list)


#---------Accessing Elements from list---
print("Accessing Elements from List")
numbers = [1, 2, 3, 4, 5]
program = ["Python", "Java", "JavaScript"]
mixed_list = [1, "apple", True, 3.14]

# Accessing elements by index
print(numbers[0])   # Output: 1
print(program[1])    # Output: Java

#---------------Modifying elements-------
program = ["Python", "Java", "JavaScript"]
program[1]= "C++"
print(program) 

#----------Adding Elements----

#---Using append() method
program = ["Python", "Java", "JavaScript"]
program.append("C++")
print(program) 

#---Using insert() method
program = ["Python", "Java", "JavaScript"]
program.insert(1, "C++")
print(program) 

#---Using extend() method

program = ["Python", "Java", "JavaScript"]
program.extend(["C++","Dart"])
print(program)

#Append list
backend = ["Python", "Java"]
frontend = ["HTML","CSS"]
backend.extend(frontend)
print(backend)

#-----Removing Elements----
#remove() Method
program = ["Python", "Java", "JavaScript"]
program.remove("Python")
print(program)

#pop() method
program = ["Python", "Java", "JavaScript"]
program.pop(2)
print(program)