# Python-Learning

![Python](images/Python4.png)

<details>
<summary><b>Getting Start with Python</b></summary>

Python is a high-level, interpreted programming language known for its simplicity and readability.Python is a popular programming language. It was created by Guido van Rossum, and released in 1991. It is used in machine learning, web development, desktop applications, and many other fields.

### <b>Getting Start with Python</b>
---

1. <code><b>Install Python:</b></code> At first, we need to download and install python. Make sure to download the latest version for our operating system.
2. <code><b>Choose a IDE:</b></code> For write our code we need to install text editor. Some popular Python IDEs include PyCharm, Visual Studio Code, and Jupyter Notebook. Visual Studio Code is better.
3. <code><b>Write First Python Program:</b></code></br>
   
    ```python
    print("Hello, Python!")
    ```
    Save this code in a file with a <code> .py </code> extension, such as <code>hello.py</code>
4. <code><b>Run Python Program:</b></code> To run Python program, open a terminal or command prompt, navigate to the directory where Python file is located, and then type python hello.py.

</details>

<details>
<summary><b>Input/Output in Python</b></summary>

### <b>Input in Python:</b>
---
<code>input(): </code>This function first takes the input from the user and converts it into a string. The type of the returned object always will be <class ‘str’>.

<b>Input Syntax:</b>

```python
name = input("Enter your name: ")

//integer or other
numer = int(input("Enter a number: "))
```

<b>For Multiple input:</b>

```python
# For multiple input
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
```

### <b>Output in Python:</b>
---
Python print() function prints the message to the screen or any other standard output device.

```python
# Displaying text output
print("Hello, World!")
```

<b>Formatting Output:</b>

```python
# Using % operator for string formatting
name = "Alice"
age = 25

print("Hello, my name is", name, "and I am", age, "years old.")

# Using f-strings (Python 3.6+)
print(f"Name: {name}, Age: {age}")
```

<b>Print Concatenated Strings</b>

```python
print('Python is a Wonderful ' + 'Programming Language.')
```

</details>

<details>
<summary><b>Python Keywords and Identifiers</b></summary>

### <b>Python Keywords:</b>
---
Python, keywords are reserved words that have special meanings and purposes. These keywords cannot be used as identifiers (such as variable names or function names) in Python programs. Here's a list of all the keywords in Python:

| False | None | True | and | as |
|---|---|---|---|---|
| assert | async | await | break | class |
| continue | def | del | elif | else |
| except | finally | for | from | global |
| if | import | in | is | lambda |
| nonlocal | not | or | pass | raise |
| return | try | while | with | yield |

<b>Print Keywords by coding:</b>

```python
import keyword

keywords = keyword.kwlist

# Print the list of keywords
print("List of Python Keywords:")
for kw in keywords:
    print(kw)
```

### <b>Python Identifiers:</b>
---
In Python, an identifier is a name given to entities like variables, functions, classes, etc. It is used to identify and refer to these entities in the code. Here are the rules for naming identifiers in Python:

+ An identifier can only contain alphanumeric characters (a-z, A-Z, 0-9) and underscores (_). It cannot start with a digit.
+ Python is case-sensitive, so myVar and myvar are different identifiers.
+ Identifiers cannot be a reserved keyword. These keywords have special meanings in Python and cannot be used as identifiers.
+ There is no limit on the length of an identifier, but it's recommended to keep it concise and meaningful.

<b>Valid Identifiers</b>

```python
my_variable
myVar
my_function
MyClass
MY_CONSTANT
```

<b>Invalid Identifiers:</b>

```python
2variable -->(starts with a digit)
my-variable -->(contains a hyphen)
if -->(reserved keyword)
my variable -->(contains a space)
```

</details>

<details>
<summary><b>Variables in Python</b></summary>
In Python, a variable is a named storage location used to store data values. Variables are created when you assign a value to them using the assignment operator =. 

+ <code><b>Variable Assignment:</b></code> In Python, variables do not need to be declared with any particular type, and can even change type after they have been set.

    ```python
    x = 10          # Assigning an integer value
    name = "Alice"  # Assigning a string value
    is_valid = True # Assigning a boolean value
    ```
+ <code><b>Variable Reassignment:</b></code> We can change the value of a variable by assigning a new value to it.
  
  ```python
    x = 4       # x is of type int
    x = "Sally" # x is now of type str
  ```

+ <code><b>Variable Type Casting:</b></code> If we want to specify the data type of a variable, this can be done with casting.
  
  ```python
    x = str(3)    # x will be '3'
    y = int(3)    # y will be 3
    z = float(3)  # z will be 3.0
  ```

+ <code><b>Getting Type of Variable:</b></code> We can get the data type of a variable with the <code>type()</code> function.

    ```python
    x = 5
    y = "John"
    print(type(x))
    print(type(y))
    ```

+ <code><b>Multiple Assignment:</b></code> We can assign values to multiple variables in a single line using multiple assignment.
  
  ```python
    x, y, z = 10, 20, 30
  ```

  ```python
    x = y = z = "Orange"
    print(x)
    print(y)
    print(z)
  ```

+ <code><b>Global Variable:</b></code> Variables that are created outside of a function (as in all of the examples above) are known as global variables.
  
  ```python
    x = "awesome"

    def myfunc():
       print("Python is " + x)

    myfunc()
  ```

  ```python
    x = "awesome"

    def myfunc():
       x = "fantastic"
       print("Python is " + x)

    myfunc()

    print("Python is " + x)
  ```

</details>

<details>
<summary><b>Data Types in Python</b></summary>
Data types are the classification or categorization of data items. It represents the kind of value that tells what operations can be performed on a particular data.

![DataType](images/Python-data-structure.jpg)

| Example                              | Data Type  |
|--------------------------------------|------------|
| x = "Hello World"                   | str        |
| x = 20                               | int        |
| x = 20.5                             | float      |
| x = 1j                               | complex    |
| x = ["apple", "banana", "cherry"]    | list       |
| x = ("apple", "banana", "cherry")    | tuple      |
| x = range(6)                         | range      |
| x = {"name" : "John", "age" : 36}    | dict       |
| x = {"apple", "banana", "cherry"}    | set        |
| x = frozenset({"apple", "banana", "cherry"}) | frozenset |
| x = True                             | bool       |
| x = b"Hello"                        | bytes      |
| x = bytearray(5)                     | bytearray |
| x = memoryview(bytes(5))             | memoryview |
| x = None                             | NoneType   |

<b>Coding Example:</b>

```python
# str
my_string = "Hello, World!"
print(my_string)

# int
my_integer = 42
print(my_integer)

# float
my_float = 3.14
print(my_float)

# complex
my_complex = 1 + 2j
print(my_complex)

# list
my_list = ["apple", "banana", "cherry"]
print(my_list)

# tuple
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# range
my_range = range(5)
print(list(my_range))

# dict
my_dict = {"name": "John", "age": 36}
print(my_dict)

# set
my_set = {"apple", "banana", "cherry"}
print(my_set)

# frozenset
my_frozenset = frozenset({"apple", "banana", "cherry"})
print(my_frozenset)

# bool
my_bool = True
print(my_bool)

# bytes
my_bytes = b"Hello"
print(my_bytes)

# bytearray
my_bytearray = bytearray(5)
print(my_bytearray)

# memoryview
my_memoryview = memoryview(b"Hello")
print(my_memoryview)

# NoneType
my_none = None
print(my_none)
```

</details>

<details>
<summary><b>Python String</b></summary>

## <b>String in Python:</b>
---
A String is a data structure in Python that represents a sequence of characters. It is an immutable data type, meaning that once we have created a string, we cannot change it. Strings in Python are created by enclosing the characters within either single quotes (') or double quotes (").

+ <code><b>Creating String:</b></code>

  ```python
  # create a string using double quotes
  str1 = "This string into double quotes"

  # create a string using single quotes
  str2 = 'This string into single quotes'

  #Print String
  print(str1)
  print(str2)
  ```

+ <code><b>Indexing & Slicing:</b></code> We can access individual characters in a string using indexing. Python uses zero-based indexing, meaning the first character is at index 0, the second at index 1,  -1 refers to the last character, -2 refers to the second last character, and so on.

  ![string](images/strings.jpg)

  ```python
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
  ```

+ <code><b>Concatenation:</b></code> Strings can be concatenated using the + operator.
  
  ```python
  str1 = "Hello"
  str2 = "World"
  result = str1 + " " + str2
  print(result)
  ```

+ <code><b>Reversing a Python String</b></code> By accessing characters from a string, we can also reverse strings in Python. We can Reverse a string by using String slicing method.
  
  ```python
  #Program to reverse a string 
  string = "PythonProgramming"
  print(string[::-1])
  ```

### <b>String Methods:</b>
---

Python provides many built-in methods to manipulate strings, such as <b>upper(), lower(), strip(), replace(), split(), join()</b>, and many more.

+ <code>capitalize():</code> Converts the first character of the string to uppercase

  ```python
  my_string = "Hello, World!"
  print(my_string.capitalize())  # Output: "Hello, world!"
  ```
+ <code>upper():</code> Converts all characters of the string to uppercase

  ```python
  my_string = "Hello, World!"
  print(my_string.upper())  # Output: "HELLO, WORLD!"
  ```

+ <code>lower():</code> Converts all characters of the string to lowercase

  ```python
  my_string = "Hello, World!"
  print(my_string.lower())  # Output: "hello, world!"
  ```

+ <code>strip():</code> Removes leading and trailing whitespace from the string

  ```python
  my_string_with_spaces = "   Hello, World!   "
  print(my_string_with_spaces.strip())  # Output: "Hello, World!"
  ```
  
+ <code>replace():</code> Replaces a specified substring with another substring

  ```python
    my_string = "Hello, World!"
    print(my_string.replace("Hello", "Hi"))  # Output: "Hi, World!"
  ```

+ <code>split():</code> Splits the string into a list of substrings based on a delimiter

  ```python
  my_string = "Hello, World!"
  print(my_string.split(", "))  # Output: ['Hello', 'World!']
  ```

+ <code>find():</code> Searches the string for a specified value and returns the position of where it was found

  ```python
  my_string = "Hello, World!"
  print(my_string.find("World"))  # Output: 7
  ```

+ <code>count():</code> Returns the number of occurrences of a specified value in the string

  ```python
  my_string = "Hello, World!"
  print(my_string.count("l"))  # Output: 3
  ```

+ <code>isalpha():</code> Returns True if all characters in the string are alphabet letters (a-z).Don't used any whitespace.

  ```python
  my_string = "Hello, World!"
  print(my_string.isalpha())  # Output: False
  
  my_string = "HelloWorld"
  print(my_string.isalpha())  # Output: True
  ```

+ <code>isnumeric():</code> Returns True if all characters in the string are numeric

  ```python
  numeric_string = "12345"
  print(numeric_string.isnumeric())  # Output: True
  ```

+ <code>startswith():</code> Returns True if the string starts with the specified value

  ```python
  my_string = "Hello, World!"
  print(my_string.startswith("Hello"))  # Output: True
  ```

+ <code>endswith():</code> Returns True if the string ends with the specified value

  ```python
  my_string = "Hello, World!"
  print(my_string.endswith("World!"))  # Output: True
  ```

+ <code>join():</code> Joins the elements of an iterable (such as a list) into a string, using the string as a separator

  ```python
  my_list = ["Hello", "World", "Python"]
  print("-".join(my_list))  # Output: "Hello-World-Python"
  ```

+ <code>format():</code> Formats the string

  ```python
  name = "Alice"
  age = 30
  print("My name is {} and I am {} years old.".format(name, age))  # Output: "My name is Alice and I am 30 years old."
  ```

+ <code>encode():</code> Encodes the string using the specified encoding

  ```python
  my_string = "Hello, World!"
  encoded_string = my_string.encode("utf-8")
  print(encoded_string)  # Output: b'Hello, World!'
  ```

+ <code>isdigit():</code> Returns True if all characters in the string are digits

  ```python
  numeric_string = "12345"
  print(numeric_string.isdigit())  # Output: True
  ```
</details>

<details>
<summary><b>Python List</b></summary>


## <b>Python List</b>
---
Python Lists are just like dynamically sized arrays, declared in other languages. Lists store multiple data together in a single variable. List items are ordered, changeable, and allow duplicate values. Lists can contain elements of different data types, and we can add, remove, or modify elements in a list.

<b>Creating list:</b></br>
---
We can create a list by enclosing comma-separated values within square brackets [ ].

```python
# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]
print(numbers)

# Creating a list of strings
program = ["Python", "Java", "JavaScript"]
print(program)

# Creating a list with mixed data types
mixed_list = [1, "apple", True, 3.14]
print(mixed_list)
```

<b>Accessing Elements from List:</b></br>
---
Each element in a list is associated with a number, known as a list index. Use the index operator [ ] to access an item in a list. The index must be an integer. Nested lists are accessed using nested indexing. 

![List](images/list-index-python.png)

```python
# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]
program = ["Python", "Java", "JavaScript"]
mixed_list = [1, "apple", True, 3.14]

# Accessing elements by index
print(numbers[0])   # Output: 1
print(program[1])    # Output: Java
```

<b>Modifying Elements:</b></br>
---

```python
# Modifying elements
program = ["Python", "Java", "JavaScript"]
program[1]= "C++"
print(program)   #output: Python, C++, JavaScript
```

<b>Adding Elemetns:</b></br>
---

We can add elements to the end of a list using the <code>append()</code> method or insert elements at a specific position using the <code>insert()</code> method.
+ <code>append():</code>  Using the append() method only one element at a time can be added to the list.
  
  ```python
  program = ["Python", "Java", "JavaScript"]
  program.append("C++")
  print(program) 
  ```
+ <code>insert():</code> The insert() method inserts an item at the specified index.
  
  ```python
  program = ["Python", "Java", "JavaScript"]
  program.insert(1, "C++")
  print(program) 
  ```
+ <code>extend():</code> This method is used to add multiple elements at the same time at the end of the list. Also used to append elements from another list to the current list.

  ```python
  program = ["Python", "Java", "JavaScript"]
  program.extend(["C++","Dart"])
  print(program)

  #Append List
  backend = ["Python", "Java"]
  frontend = ["HTML","CSS"]
  backend.extend(frontend)
  print(backend)
  ```

### <b>Removing Elements:</b>
---
We can remove elements from a list using the <code>remove()</code> method to remove a specific value, or the <code>pop()</code> method to remove an element by index.

+ <code>remove():</code> Remove() method only removes one element at a time, to remove a range of elements, the iterator is used. The remove() method removes the specified item.

  ```python
  program = ["Python", "Java", "JavaScript"]
  program.remove("Python")
  print(program)
  ```

+ <code>pop():</code> function can also be used to remove and return an element from the list, but by default it removes only the last element of the list, to remove an element from a specific position of the List, the index of the element is passed as an argument to the pop() method.

  ```python
  program = ["Python", "Java", "JavaScript"]
  program.pop(2)
  print(program)
  ```

+ <code>del:</code> The `del` keyword also removes the specified index. The `del` keyword can also delete the list completely

  ```python
  thislist = ["apple", "banana", "cherry"]
  del thislist[0]

  #Delete the list
  del thislist
  ```

+ <code>clear():</code> The clear() method empties the list. The list still remains, but it has no content.

  ```python
  thislist = ["apple", "banana", "cherry"]
  thislist.clear()
  ```

<b>Sort List:</b></br>
---
In Python, we can sort a list using the sort() method or the built-in sorted() function.

+ <code>sort():</code> The sort() method sorts the list in place, it modifies the original list.
  
  ```python
  my_list = [3, 1, 4, 1, 5, 9, 2, 6]
  my_list.sort()
  print("Sorted list:", my_list)

  program = ["Python", "Java", "Dart", "JavaScript", "C++"]
  program.sort()
  print("Sorted list:",program)
  ```

  Sort the list in descending order

  ```python
  # Sort the list in descending order
  my_list = [3, 1, 4, 1, 5, 9, 2, 6]
  my_list.sort(reverse=True)
  print("Sorted list:", my_list)

  program = ["Python", "Java", "Dart", "JavaScript", "C++"]
  program.sort(reverse=True)
  print("Sorted list:",program)
  ```
+ <code>sorted():</code> The sorted() function returns a new sorted list without modifying the original list.

  ```python
  my_list = [3, 1, 4, 1, 5, 9, 2, 6]
  sort_list = sorted(my_list)
  print("Sorted list:", sort_list)

  program = ["Python", "Dart", "JavaScript", "C++"]
  sort_list2 = sorted(program, reverse= True)
  print("Sorted list:",sort_list2)
  ```

<b>Copy List:</b></br>
---
To copy a list in Python, we have a couple of options. We can use the copy() method, or we can use slicing or the list() constructor. We cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

```python
program = ["Python", "Dart", "JavaScript", "C++"]
new_program = program.copy()
print(new_program)
```

Another way to make a copy is to use the built-in method list()

```python
program = ["Python", "Dart", "JavaScript", "C++"]
new_program = list(program)
print(new_program)
```

</details>
