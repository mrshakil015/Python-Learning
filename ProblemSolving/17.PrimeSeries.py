# prime number series

user_input = int(input("Enter the size of series: "))
prime_numbers=[]
for x in range(user_input):
    if x%2!=0:
        if x==1:
            x+=1
        prime_numbers.append(x)
print(prime_numbers)



