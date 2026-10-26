#random password generator

import random
import string
from tabnanny import check

characters = string.ascii_letters + string.digits + string.punctuation
minimum_length = 12

def generate_password(length):
    password = ''
    for _ in range(length):
        password += random.choice(characters)

    return password

#finnaly password is generated
print("Your generated password is: " + generate_password(minimum_length))

print("you can use this password to secure your accounts and keep your information safe.")
    
