# Определить, положительное число, отрицательное или ноль.

x = float(input("Enter a number: "))
if x == 0:
    print("It's zero.")
elif x > 0:
    print("It's positive.")
else:
    print("It's negative.")
    