# Summation of List Value
lsize = int(input("Enter the list size: "))

mylist =[]
summation = 0

for i in range(lsize):
    value = int(input())
    mylist.append(value)
    summation+=value
    
print("My list is: ",mylist)
print("Summation of the list: ",summation)