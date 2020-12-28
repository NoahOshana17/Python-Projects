import random
import string


def password_generator():
    password = [random.choice(string.ascii_letters) for i in range(10)]
    return ''.join(password)

#password = [random.choice(string.ascii_letters) for i in range(10)]
#print(password)

print(password_generator())
