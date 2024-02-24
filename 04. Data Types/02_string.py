# create a string using double quotes
str1 = "This string into double quotes"

# create a string using single quotes
str2 = 'This string into single quotes'

print(str1)
print(str2)


#----Accessing Character in Python String----

str1 = "PythonProgramming"
print("Initial String: ") 
print(str1) 

# Printing First character 
print("\nFirst character of String is: ") 
print(str1[0]) 

# Printing Last character 
print("\nLast character of String is: ") 
print(str1[-1]) 

# Printing Specific Range
print("\nSpecific Range of String is: ") 
print(str1[6:]) 

# Printing characters between 
print("\nSlicing characters between 3rd and 2nd last character: ") 
print(str1[3:-2])

#Program to reverse a string 
print(str1[::-1])

#---String Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)