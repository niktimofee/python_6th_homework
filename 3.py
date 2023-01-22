# 📍 Программа, которая находит произведение пар чисел списка 
# (парой считаем первый и последний, второй предпоследний и тд).
#
# (улучшение с помощью использования лямбд, filter, map, zip, enumerate, list comprehension)

import random

rand_list = [random.randint(1, 10) for i in range(5)]
result = [rand_list[num_index] * rand_list[-num_index-1] for num_index in range(len(rand_list) // 2 + len(rand_list) % 2)]
print(f'📜 Список произведений чисел с конца и чисел с начала списка {rand_list} => {result}')