# 2 task

number = float(input())
if number == int(number):
    print(f"Ваше число {number} является целым")
    if number % 2 == 0:
        print(f"Ваше число {number} является четным")
    else:
        print(f"Ваше число {number} является нечетным")
    if number > 0:
            print(f"Ваше число {number} является положительным")
    elif number < 0:
            print(f"Ваше число {number} является отрицательным")
    else:
            print("Ваше число равно нулю")
    if 10 <= number <= 50:
            print(f"Ваше число {number} принадлежит диапазону [10, 50]")
    else:
            print(f"Ваше число {number} не принадлежит диапазону [10, 50]")
else:
    print(f"Ваше число {number} является нецелым")
    if number > 0:
        print(f"Ваше число {number} является положительным")
    elif number < 0:
        print(f"Ваше число {number} является отрицательным")
    else:
        print("Ваше число равно нулю")
    if 10 <= number <= 50:
        print(f"Ваше число {number} принадлежит диапазону [10, 50]")
    else:
        print(f"Ваше число {number} не принадлежит диапазону [10, 50]")
