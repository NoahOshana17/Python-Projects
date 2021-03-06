import random
import string


class PasswordGenerator:
    def __init__(self, length=10, capital_letters=True, digits=False, special_char=False):
        self.length = length
        self.capital_letters = capital_letters
        self.digits = digits
        self.special_char = special_char
        self.password = ''

    def generate_password(self):
        if self.capital_letters and self.digits and self.special_char:
            self.password = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for i in
                                     range(self.length)])
        elif self.capital_letters and self.digits and not self.special_char:
            self.password = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(self.length)])
        elif self.capital_letters and not self.digits and not self.special_char:
            self.password = ''.join([random.choice(string.ascii_letters) for i in range(self.length)])
        elif not self.capital_letters and self.digits and self.special_char:
            self.password = ''.join([random.choice(string.ascii_lowercase + string.digits + string.punctuation) for i in
                                     range(self.length)])
        elif not self.capital_letters and not self.digits and not self.special_char:
            self.password = ''.join([random.choice(string.ascii_letters) for i in range(self.length)]).lower()
        else:
            self.password = "test"

        return self.password

    def generate_password2(self):
        result = int(self.capital_letters)
        result = (result << 1) + int(self.digits)
        result = (result << 1) + int(self.special_char)

        if result == 0:
            self.password = ''.join([random.choice(string.ascii_lowercase) for i in range(self.length)])
        elif result == 1:
            self.password = ''.join([random.choice(string.punctuation) for i in range(self.length)])
        elif result == 2:          #add lowercase letters by default so password isnt just numbers
            self.password = ''.join([random.choice(string.ascii_lowercase + string.digits) for i in range(self.length)])
        elif result == 3:
            self.password = ''.join([random.choice(string.digits + string.punctuation) for i in range(self.length)])
        elif result == 4:
            self.password = ''.join([random.choice(string.ascii_uppercase) for i in range(self.length)])
        elif result == 5:
            self.password = ''.join([random.choice(string.ascii_uppercase + string.punctuation) for i in range(self.length)])
        elif result == 6:
            self.password = ''.join([random.choice(string.ascii_uppercase + string.digits) for i in range(self.length)])
        elif result == 7:
            self.password = ''.join([random.choice(string.ascii_uppercase + string.digits + string.punctuation)
                                     for i in range(self.length)])
        else:
            self.password = ''

        return self.password

    def get_info(self):
        self.length = int(input("Enter your desired length for the password: "))

        capital_letters = input("Would you like capital letters in your password? (y) or (n) ").upper()
        if capital_letters == 'Y':
            self.capital_letters = True
        elif capital_letters == 'N':
            self.capital_letters = False
        else:
            print("Error. Password will not have capital letters...")
            self.capital_letters = False

        digits = input("Would you like digits in your password? (y) or (n) ").upper()
        if digits == 'Y':
            self.digits = True
        elif digits == 'N':
            self.digits = False
        else:
            print("Error. Password will not have digits...")
            self.digits = False

        special_char = input("Would you like special characters in your password? (y) or (n) ").upper()
        if special_char == 'Y':
            self.special_char = True
        elif special_char == 'N':
            self.special_char = False
        else:
            print("Error. Password will not have special characters...")
            self.special_char = False

    def __repr__(self):
        return self.password


password = PasswordGenerator()
password.get_info()
password.generate_password2()
print(password)
