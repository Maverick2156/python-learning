a = int(input("Enter year of birth: "))
b = int(input("Enter current year: "))
if b < a:
    print("Error: Current year can't be less than year of birth.")
else:
    age = int(b - a)
    if age < 0:
        print("Error: Year of birth can't be greater than the current year.")
    else:
        print(f"You are {age} years old.")