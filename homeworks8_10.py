count_five = 0
number_my = ''
while not number_my.isdigit():
    number_my = input('введите число: ')
for counter in range(len(number_my)):
    number = int(number_my[counter])
    if number == 5:
        count_five += 1

lenth_finish = len('В числе ' + number_my + '  ' + str(count_five) + '5-ки')
lenth_finish1 = len('Цифры 5 нет в числе ' + number_my)

if count_five != 0:
    print('*' * lenth_finish)
    print('В числе', number_my, count_five, '5-ки')
    print('*' * lenth_finish)
else:
    print('*' * lenth_finish1)
    print('Цифры 5 нет в числе', number_my)
    print('*' * lenth_finish1)

