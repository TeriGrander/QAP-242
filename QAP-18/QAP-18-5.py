todo_list = [# утро  день  вечер
            ['',    '',    ''], # понедельник
            ['',    '',    ''], # вторник
            ['',    '',    ''], # среда
            ['',    '',    ''], # четверг
            ['',    '',    ''], # пятница
            ['',    '',    ''], # суббота
            ['',    '',    ''], # воскресенье
           ]
for i in range(len(todo_list)):
    for j in range(len(todo_list[i])):
        todo_list[i][j] = input('дело: ')
rem = int(input('Что удалить? '))
todo_list.pop(rem-1)

day_add = int(input('В какой день добавлять? '))
item = input('Какое дело? ')

todo_list[day_add-1].append(item)

for i in range(len(todo_list)):
    for j in range(len(todo_list[i])):
        print(todo_list[i][j], end = ' ')
    print('', end = '\n')