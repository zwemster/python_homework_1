list_subsequence = []
for i in range(1, int(input('Какая будет степень последовательности? ')) + 1):
    subsequence = (1 + 1 / i) ** i
    list_subsequence.append(round(subsequence, 2))
print(f'Сумма элементов списка {list_subsequence} будет равна {sum(list_subsequence)}')
