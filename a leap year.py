x = int(input("Enter a year: "))

if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
    print(f"{x} is a leap year.")
else:
    print(f"{x} is not a leap year.")