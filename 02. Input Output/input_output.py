# For single input
name = input("Enter your name: ")

# For multiple input
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)

#Formating output
# Using % operator for string formatting
name = "Alice"
age = 25
print("Hello, my name is", name, "and I am", age, "years old.")


# Using f-strings (Python 3.6+)
print(f"Name: {name}, Age: {age}")