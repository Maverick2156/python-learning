year_of_birth = int(input("Enter year of birth: "))
current_year = int(input("Enter current year: "))
if current_year < year_of_birth:
    print("Error: Current year can't be less than year of birth.")
else:
    age = int(current_year - year_of_birth)
    if age < 0:
        print("Error: Year of birth can't be greater than the current year.")
    else:
        print(f"You are {age} years old.")