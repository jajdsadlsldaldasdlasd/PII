# 3 task

import random
import string

spec_symbols = "!@#$%^&*"
alph = string.printable[36:62]
nums = '0123456789'

password_chars = []
password_chars += random.choices(spec_symbols, k=2)
password_chars += random.choices(alph, k=3)
password_chars += random.choices(nums, k=3)
random.shuffle(password_chars)

password = ''.join(password_chars)

print(password)
