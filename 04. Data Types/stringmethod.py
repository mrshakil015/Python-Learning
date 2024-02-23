# Example string
my_string = "Hello, World!"

# 1. capitalize(): Converts the first character of the string to uppercase
print(my_string.capitalize())  # Output: "Hello, world!"

# 2. upper(): Converts all characters of the string to uppercase
print(my_string.upper())  # Output: "HELLO, WORLD!"

# 3. lower(): Converts all characters of the string to lowercase
print(my_string.lower())  # Output: "hello, world!"

# 4. strip(): Removes leading and trailing whitespace from the string
my_string_with_spaces = "   Hello, World!   "
print(my_string_with_spaces.strip())  # Output: "Hello, World!"

# 5. replace(): Replaces a specified substring with another substring
print(my_string.replace("Hello", "Hi"))  # Output: "Hi, World!"

# 6. split(): Splits the string into a list of substrings based on a delimiter
print(my_string.split(", "))  # Output: ['Hello', 'World!']

# 7. find(): Searches the string for a specified value and returns the position of where it was found
print(my_string.find("World"))  # Output: 7

# 8. count(): Returns the number of occurrences of a specified value in the string
print(my_string.count("l"))  # Output: 3

# 9. isalpha(): Returns True if all characters in the string are alphabetic
print(my_string.isalpha())  # Output: False

# 10. isnumeric(): Returns True if all characters in the string are numeric
numeric_string = "12345"
print(numeric_string.isnumeric())  # Output: True

# 11. startswith(): Returns True if the string starts with the specified value
print(my_string.startswith("Hello"))  # Output: True

# 12. endswith(): Returns True if the string ends with the specified value
print(my_string.endswith("World!"))  # Output: True

# 13. join(): Joins the elements of an iterable (such as a list) into a string, using the string as a separator
my_list = ["Hello", "World", "Python"]
print("-".join(my_list))  # Output: "Hello-World-Python"

# 14. format(): Formats the string
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))  # Output: "My name is Alice and I am 30 years old."

# 15. encode(): Encodes the string using the specified encoding
encoded_string = my_string.encode("utf-8")
print(encoded_string)  # Output: b'Hello, World!'

# 16. isdigit(): Returns True if all characters in the string are digits
numeric_string = "12345"
print(numeric_string.isdigit())  # Output: True
