x = float(input("What's x? "))
y = float(input("What's y? "))

if y == 0:
    w = "Error: Division by zero is not allowed."
else:
    w = round(x / y, 2)

z = round(x + y, 2)
q = round(x - y, 2)
v = round(x * y, 2)

def print_results():
    print(f"Sum: {z}")
    print(f"Difference: {q}")
    print(f"Product: {v}")
    print(f"Quotient: {w}")
print_results()
