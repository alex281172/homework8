count_max = 0
number_my = ''
while not number_my.isdigit():
    number_my = input('введите число: ')
for counter in range(len(number_my)):
    number = int(number_my[counter])
    if number > count_max:
        count_max = number
lenth_finish = len(' - максимальная цифра ' + ' в числе: ' + number_my)
print('*' * lenth_finish)
print(count_max, '- максимальная цифра', 'в числе:', number_my)
print('*' * lenth_finish)