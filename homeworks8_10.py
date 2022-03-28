count_five = 0
number_my = ''
while not number_my.isdigit():
    number_my = input('введите число: ')
for counter in range(len(number_my)):
    number = int(number_my[counter])
    if number == 5:
        count_five += 1
print('*' * 30)
if count_five != 0:
    print("В числе", number_my, count_five, '5-ки')
else:
    print("Цифры 5 нет в числе", number_my)
print('*' * 30)
