def V(S, t):
    return S/t

S = float(input("Enter the distance in km: "))
t = float(input("Enter the time in hours: "))

if t == 0:
    print("Time can't be zero. Please enter a valid time.")
else:
    print(f"The speed is {V(S, t):.2f} km/h.")
