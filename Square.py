# Функция для вычисления площади четырехугольника
def square(length, width):
    return length * width

# Функция для вычисления периметра четырехугольника
def perimeter(length, width):
    return 2 * (length + width)

# Ввод длины и ширины четырехугольника
a = float(input("Enter the Length in cm: "))
b = float(input("Enter the Width in cm: "))

# Вычисление площади и периметра
sq_result = square(a, b)
per_result = perimeter(a, b)

# Вывод результатов
print(f"The square {sq_result} cm².")
print(f"The perimeter {per_result} cm.")