# Password Generator Program

import random
import string

print("Welcome to the Password Generator!\n")

# Get desired password length from user
try:
    length = int(input("Enter the desired password length: "))
    if length <= 0:
        print("Password length must be a positive number.")
        exit()
except ValueError:
    print("Please enter a valid number.")
    exit()

# Define possible characters (letters, digits, symbols)
chars = string.ascii_letters + string.digits + string.punctuation

# Generate the password
password = ''.join(random.choice(chars) for _ in range(length))

# Display the result
print(f"\nYour generated password is:\n{password}")
