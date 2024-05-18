lsize = int(input("Enter the list size: "))

mylist =[]
uniquelist = []
duplicatelist = []


for i in range(lsize):
    value = int(input())
    mylist.append(value)

for item in mylist:
    if item not in uniquelist:
        uniquelist.append(item)
    else:
        duplicatelist.append(item)
        
print("My List is: ",mylist)
print("Uniquelist is: ",uniquelist)
print("Duplicate is: ",duplicatelist)