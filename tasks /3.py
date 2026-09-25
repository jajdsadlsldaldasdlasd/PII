# 3 task

import random
import string

spec_symbols = "!@#$%^&*"
alph = string.printable[36:62]
nums = '0123456789'

password = ""

password += ''.join(random.choices(spec_symbols, k=2))
password += ''.join(random.choices(alph, k=3))
password += ''.join(random.choices(nums, k=3))

print(password)
