x = float(input("What's x? "))
y = float(input("What's y? "))

if y == 0:
    w = "Error: Division by zero is not allowed."
else:
    w = round(x / y, 2)

z = round(x + y, 2)
q = round(x - y, 2)
v = round(x * y, 2)

print(f"Sum: {z}, Difference: {q}, Product: {v}, Quotient: {w}")