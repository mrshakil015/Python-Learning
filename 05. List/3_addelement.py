#----------Adding Elements----

#---Using append() method
program = ["Python", "Java", "JavaScript"]
program.append("C++")
print(program) 

#---Using insert() method
program = ["Python", "Java", "JavaScript"]
program.insert(1, "C++")
print(program) 

#---Using extend() method

program = ["Python", "Java", "JavaScript"]
program.extend(["C++","Dart"])
print(program)

#Append list
backend = ["Python", "Java"]
frontend = ["HTML","CSS"]
backend.extend(frontend)
print(backend)