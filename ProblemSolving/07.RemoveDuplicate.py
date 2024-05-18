lsize = int(input("Enter the list size: "))

mylist =[]
count = 0

for i in range(lsize):
    value = int(input())
    mylist.append(value)

for i in mylist:
    temp = i
    for j in mylist:
        if temp == j:
            count+=1
            if count>1:
                mylist.remove(j)
    count=0
print("Unique list is: ",mylist)