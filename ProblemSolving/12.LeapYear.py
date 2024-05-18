#------------- Leap Year ---------------

year = int(input("Enter a year: "))

if (year % 2 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
    print(f"{year} is a Leap year")
else:
    print(f"{year} is not Leap year")
