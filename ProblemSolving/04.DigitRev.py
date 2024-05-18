# Reverse the number

value = int(input("Enter a value: "))
rem = 0

while True:
    temp = value // 10
    val = value % 10    
    rem = rem * 10 + val
    value = temp
    if temp == 0:
        break

print("Reverse digit: ",rem)

