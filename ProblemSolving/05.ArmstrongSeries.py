sizeseries = int(input("Enter a size: "))

for value in range(sizeseries):
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
        print(arms, end=' ')
    