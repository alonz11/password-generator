import random
import string
print("enter the password length: ")
password_length = int(input())
password = [''] * password_length
for i in range(password_length):
    password[i]=random.choice(string.digits+string.ascii_letters)

password = '' .join(password)
print(password)