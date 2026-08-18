# Function to calculate the square of a radius
import math

def sq(r):
    return r * r

r = float(input("Enter the radius of the circle in cm: "))

sq_circle = math.pi * sq(r)

print(f"The area of the circle is {sq_circle:.3f} cm².") 