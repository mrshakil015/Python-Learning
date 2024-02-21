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