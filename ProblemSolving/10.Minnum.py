# Find Minimum number from the list.
lsize = int(input("Enter the list size: "))

mylist =[]

for i in range(lsize):
    value = int(input())
    mylist.append(value)

minnum = mylist[0]   

for value in mylist:
    if value < minnum:
        minnum = value
        
print("List is: ",mylist)       
print("Minimum Number is: ",minnum)
    