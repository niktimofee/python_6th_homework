# 📍 Программа, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
#
# (улучшение с помощью использования лямбд, filter, map, zip, enumerate, list comprehension)

a = [int(input(f'✏️  Введите "{i}" координату для точки "a": ')) for i in "xy"]
b = [int(input(f'✏️  Введите "{i}" координату для точки "b": ')) for i in "xy"]
result = sum([(element[1] - element[0])**2 for element in zip(a, b)])**0.5
print(f'📏 Расстояние между точками "a" и "b" в 2D пространстве = {result}')