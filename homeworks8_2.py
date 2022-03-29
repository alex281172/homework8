digit_five = 0
for counter in range(1, 11, 1):
    print('введите ЦИФРУ №', counter, ' из 10:', sep='')
    digital_new = input()
    print('-' * 30)
    while not digital_new.isdigit() or int(digital_new) < 0 or int(digital_new) >= 10:
        print('введите еще раз цифру №', counter, ' (от 0 до 9):   ', sep='')
        digital_new = input()
        print('-' * 30)
    else:
        if int(digital_new) == 5:
            digit_five += 1
print('конец цикла')
print('*' * 18)
print('введено ', digit_five, 'пятерок')
print('*' * 18)