digit_five = 0
for counter in range(1, 11, 1):
    print('введите ЦИФРУ №', counter, ':', sep='')
    digital_new = input()
    print('-' * 20)
    while not digital_new.isdigit() or int(digital_new) < 0 or int(digital_new) >= 10:
        print('введите еще раз цифру №', counter, ' (от 0 до 9):   ', sep='')
        digital_new = input()
        print('-' * 20)
    else:
        if int(digital_new) == 5:
            digit_five += 1
print('конец цикла')
print('*' * 20)
print('введено ', digit_five, 'пятерок')
print('*' * 20)