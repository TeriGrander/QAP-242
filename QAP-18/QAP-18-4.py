n = input('Сколько дел запланировано на сегодня? ')
todo = []
for i in range(int(n)):
    t = input('Введите дело: ')
    todo.append(t)
print('Список дел на сегодня:')
for i in range(int(n)):
    print(f'{i+1}. {todo[i]}')
ed = input('Какое дело отредактировать? ')
todo[int(ed)-1] = input(f'Введите новое описание дела {ed}: ')
rem = input('Какое дело удалить? ')
todo.pop(int(rem)-1)
print('Список дел на сегодня:')
for i in range(len(todo)):
    print(f'{i+1}. {todo[i]}')