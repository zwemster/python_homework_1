list_factorial = []
factorial = 1
for i in range(1, int(input('Сколько факториалов? ')) + 1):
    factorial *= i
    list_factorial.append(factorial)
print(list_factorial)
