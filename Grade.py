x = int(input("Enter a number between 1 and 100: "))

if (x >= 90) or (x == 100):
    print(" Your grade is A.")
elif (x >= 80) and (x < 90):
    print(" Your grade is B.")
elif (x >= 70) and (x < 80):
    print(" Your grade is C.")
elif (x >= 60) and (x < 70):
    print(" Your grade is D.")
else:
    print(" Your grade is F.")