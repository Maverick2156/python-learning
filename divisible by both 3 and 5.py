x = int(input("Enter a number: "))

if x % 3 == 0 and x % 5 == 0:
    print(f"{x} is divisible by both 3 and 5.")
elif x % 3 == 0:
    print(f"{x} is divisible by 3 but not by 5.")
elif x % 5 ==0:
    print(f"{x} is divisible by 5 but not 3.")