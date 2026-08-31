x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
z = float(input("Enter the third number: "))

if x > y and x > z:
    print(f"The largest number is: {x}")
elif y > x and y > z:
    print(f"The largest number is: {y}")
else:
    print(f"The largest number is: {z}")
if x== y and x == z:
    print("All three numbers are equal.")