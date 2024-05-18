# Find Maximum number from the list.
lsize = int(input("Enter the list size: "))

mylist =[]

for i in range(lsize):
    value = int(input())
    mylist.append(value)

maxnum = mylist[0]   

for value in mylist:
    if value > maxnum:
        maxnum = value
        
print("List is: ",mylist)       
print("Maximum Number is: ",maxnum)
    