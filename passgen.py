import random
import string

password_length = int(input("pass length "))
def generate(len=password_length):
    passw = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choise(passw) for i in range(len))

password = generate(password_length)
print(password)
