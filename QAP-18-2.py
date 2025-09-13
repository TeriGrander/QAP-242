coworkers = ['Юра','Олег','Алексей','Михаил','Андрей']

print(f'Первый: {coworkers[0]}')
print(f'Последний: {coworkers[-1]}')
print(f'Каждый первый (то есть, все): ', end='')
print(coworkers[::])
print(f'Каждый второй: {coworkers[1::2]}')
print(f'Количество: {len(coworkers)}')
new_person = input('Введите имя нового коллеги: ')
coworkers.append(new_person)
print(f'Теперь с вами работают {len(coworkers)} человек')
check_person = input('Введите имя для проверки: ')
if check_person in coworkers: print('Да, это ваш коллега')
else: print('Нет, этот человек с вами не работает')

# test changes for lesson about git