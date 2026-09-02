pass_word = str("QWERTY")
log_in = str("QWE")

x = str(input("Sign in:"))
y = str(input("Password:"))

if (x == pass_word) and (y == log_in):
    print("Access allowed.")
elif (x != pass_word) or (y != log_in):
    print("Access denied.")
else:
    print("Access denied.")