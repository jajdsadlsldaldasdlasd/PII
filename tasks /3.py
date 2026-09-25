# 3 task

import random
import string

spec_symbols = "!@#$%^&*"
alphabet = string.printable[36:62]
numbers = '0123456789'

password_chars = []
password_chars += random.choices(spec_symbols, k=2)
password_chars += random.choices(alphabet, k=3)
password_chars += random.choices(numbers, k=3)
random.shuffle(password_chars)

password = ''.join(password_chars)

print(password)
