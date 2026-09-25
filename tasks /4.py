# 4 task

from collections import Counter

input_line = str(input("Введите вашу строку").lower()).replace(" ", "")

most_common_symbol = Counter(input_line).most_common(1)
second_most_common_symbol = Counter(input_line).most_common(2)
third_most_common_symbol = Counter(input_line).most_common(3)

print(f"Первый по частоте символ: {most_common_symbol[0][0]}, он встретился {most_common_symbol[0][1]} раз")  
print(f"Второй по частоте символ: {second_most_common_symbol[1][0]}, он встретился {second_most_common_symbol[1][1]} раз")  
print(f"Третий по частоте символ: {third_most_common_symbol[2][0]}, он встретился {third_most_common_symbol[2][1]} раз")
