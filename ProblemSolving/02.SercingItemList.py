#Searcing Item from list

lsize = int(input("Enter the list size: "))
searchitem = int(input("Enter the item: "))

mylist =[]
indx = 0

for i in range(lsize):
    value = int(input())
    mylist.append(value)
print("My list is: ",mylist)

for item in mylist:
    
    if searchitem == item:
        print(f"Item {searchitem} found on index {indx}")
    indx+=1
