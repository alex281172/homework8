summ_digit = 1
number_my = ''
while not number_my.isdigit():
    number_my = input('введите число: ')
for counter in range(len(number_my)):
    number = int(number_my[counter])
    summ_digit = summ_digit * number
    print(number)

print('*' * 20)
print("произведение всех цифр числа ", number_my, ':  ', summ_digit, sep='')