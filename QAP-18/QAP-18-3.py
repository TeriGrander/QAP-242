family = ('Елена', 'Виктор', 'Аня')
print(f'Нулевой элемент: {family[0]}, последний элемент: {family[-1]}')
print(f'Чётные элементы: {family[::2]}')
print(f'Длина кортежа: {len(family)}')

numbers = {0,1,2,3,4,5,6,7,8,9}
check = input('Введите число: ')
if int(check) in numbers:
    print('Число есть во множестве, удаляем.')
    numbers.remove(int(check))
else:
    print('Числа нет во множестве, добавляем.')
    numbers.add(int(check))

print(f'Теперь длина множества: {len(numbers)}, само множество: {numbers}')
