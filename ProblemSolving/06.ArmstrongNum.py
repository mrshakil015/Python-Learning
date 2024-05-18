value = int(input("Enter a value: "))
arvalue = value
sizeval = len(str(value))

arms = 0

while True:
    temp = value // 10
    remi = value % 10
    arms += remi ** sizeval
    value = temp
    
    if temp == 0:
        break
if arvalue == arms:
    print(f"{arvalue} is Armstrong Number.")
else:
    print(f"{arvalue} is not Armstrong Number.")