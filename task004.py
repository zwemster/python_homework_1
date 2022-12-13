import random

basic_list = list(range(1, int(input('Список из скольки элементов нужен? ')) + 1))
print(f'Исходный список: {basic_list}')
random.shuffle(basic_list)
print(f'А вот перемешанный список: {basic_list}')
