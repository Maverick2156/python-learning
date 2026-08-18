def square(length, width):
    return length * width

def perimeter(length, width):
    return 2 * (length + width)

a = float(input("Enter the Length in cm: "))
b = float(input("Enter the Width in cm: "))
sqresult = square(a, b)
perimeter_result = perimeter(a, b)
print(f"The square {sqresult} cm².")
print(f"The perimeter {perimeter_result} cm.")