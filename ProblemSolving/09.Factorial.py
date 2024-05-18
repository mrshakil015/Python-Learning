# Factorial Number Calculation

value = int(input("Enter a value: "))
temp = value
i =0
fact =1
print("Factorial Series: ")
while temp > i:
    if temp == 1:
        print(temp)
    else:
        print(temp, end='*')
    fact *=temp
    temp -=1
print(f"Factroial Number of {value} is: {fact}")
    