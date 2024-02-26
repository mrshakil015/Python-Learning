#--------sort() method---------
my_list = [3, 1, 4, 1, 5, 9, 2, 6]
my_list.sort()
print("Sorted list:", my_list)

program = ["Python", "Java", "Dart","JavaScript", "C++"]
program.sort()
print("Sorted list:",program)

# Sort the list in descending order
my_list = [3, 1, 4, 1, 5, 9, 2, 6]
my_list.sort(reverse=True)
print("Sorted list:", my_list)

program = ["Python", "Java", "Dart", "JavaScript", "C++"]
program.sort(reverse=True)
print("Sorted list:",program)


#--------sorted() method---------
my_list = [3, 1, 4, 1, 5, 9, 2, 6]
sort_list = sorted(my_list)
print("Sorted list:", sort_list)

program = ["Python", "Dart", "JavaScript", "C++"]
sort_list2 = sorted(program, reverse= True)
print("Sorted list:",sort_list2)