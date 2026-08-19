def V(S, t):
    return S/t

S = float(input("Enter the distance in km: "))
t = float(input("Enter the time in hours: "))

print(f"The speed is {V(S, t):.2f} km/h.")
