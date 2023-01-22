# 📍 Программа, которая находит сумму чисел списка стоящих на нечётной позиции.
#
# (улучшение с помощью использования лямбд, filter, map, zip, enumerate, list comprehension)

import random

rand_list = [random.randint(1, 20) for i in range(7)]
result = sum([num for num_index, num in enumerate(rand_list) if num_index % 2 == 1])
print(f'Сумма чисел стоящих на нечётных позициях из списка {rand_list} равна {result}')