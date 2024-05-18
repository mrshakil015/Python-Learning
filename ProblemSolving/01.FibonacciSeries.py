# Fibonacci Series
num_terms = int(input("Enter the size of series: "))

a = 0
b = 1
count = 0

print(f"Fibonacci series up to {num_terms} terms:")

while count < num_terms:
    print(a, end=' ')
    next_value = a + b
    a = b
    b = next_value
    count += 1
