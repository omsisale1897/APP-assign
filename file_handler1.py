
import re

password = input("Enter your password: ")

pattern = r'^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*]).{8,}$'

if re.match(pattern, password):
    print("Password is Valid")
else:
    print("Password is Invalid")
    print("Password must contain:")
    print("1. At least 8 characters")
    print("2. At least one uppercase letter")
    print("3. At least one digit")
    print("4. At least one special character (!@#$%^&*)")
