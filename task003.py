symmetric_list = []
list_size = int(input('В каком диапазоне составить симметричную относительно нуля последовательность? '))
for i in range(list_size * (-1), list_size + 1):
    symmetric_list.append(i)
print(symmetric_list)

elements_product = 1
for i in list("".join(input("Элементы под какими индексами перемножить? ").split(" "))):
    elements_product *= symmetric_list[int(i)]
print(f'Сумма выбранных элементов равна {elements_product}')
