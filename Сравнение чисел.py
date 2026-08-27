# Вывести большее из двух чисел; при равенстве вывести сообщение

x = float(input("Enter a number: "))
y = float(input("Enter a number: "))

if x == y:
    print(f"{x} and {y} are equal.")
elif x > y:
    print(f"{x} is bigger than {y}.")
else:
    print(f"{y} is bigger than {x}.")