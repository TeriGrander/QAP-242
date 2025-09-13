import random
# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students: # 1 итерация: student = 'Александра'
    students_marks[student] = {} # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes: # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1,5) for i in range(3)] # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
    {students_marks[student]}''')


commands_list = ('''
      Список команд:
      1. Добавить оценки ученика по предмету
      2. Вывести средний балл по всем предметам по каждому ученику
      3. Вывести все оценки по всем ученикам
      4. Добавить ученика
      5. Редактировать имя ученика
      6. Удалить ученика
      7. Добавить предмет
      8. Редактировать название предмета
      9. Удалить предмет
      10. Редактировать оценки ученика по предмету
      11. Вывести все оценки ученика по предмету
      12. Вывести все оценки ученика по всем предметам
      13. Вывести средний балл ученика по каждому предмету
      14. Вывести средний балл ученика по определённому предмету
      15. Выход из программы
''')

while True:
    print(commands_list)
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum//marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Добавить ученика')
        students.append(input('Введите имя нового ученика: '))
    elif command == 5:
        print('5. Редактировать имя ученика')
        student_to_edit = input('Введите имя ученика, которое нужно отредактировать: ')
        if student_to_edit in students: 
            new_name = input('Введите новое имя: ')
            ind = students.index(student_to_edit)
            students[ind] = new_name
            students_marks[new_name] = students_marks[student_to_edit]
            del students_marks[student_to_edit]
        else: print('Такого ученика в журнале нет')
    elif command == 6:
        print('6. Удалить ученика')
        student_to_del = input('Введите имя ученика, которого нужно удалить из журнала: ')
        if student_to_del in students: 
            students.remove(student_to_del)
            del students_marks[student_to_del]
        else: print('Такого ученика в журнале нет')
    elif command == 7:
        print('7. Добавить предмет')
        new_class = input('Введите название нового предмета: ')
        classes.append(new_class)
        for student in students_marks.values():
            student[new_class] = []
    elif command == 8:
        print('8. Редактировать название предмета')
        class_to_edit = input('Введите название предмета, которое нужно отредактировать: ')
        if class_to_edit in classes: 
            new_name = input('Введите новое название: ')
            ind = classes.index(class_to_edit)
            classes[ind] = new_name
            for marks in students_marks.values():
                marks[new_name] = marks[class_to_edit]
                del marks[class_to_edit]
        else: print('Такого предмета в журнале нет')
    elif command == 9:
        print('9. Удалить предмет')
        class_to_del = input('Введите название предмета, который нужно удалить: ')
        if class_to_del in classes: 
            classes.remove(class_to_del)
            for marks in students_marks.values():
                if class_to_del in marks.keys(): del marks[class_to_del]
        else: print('Такого предмета в журнале нет')
    elif command == 10:
        print('10. Редактировать оценки ученика по предмету')
        edit_marks_student = input('Введите имя ученика, чьи оценку нужно изменить: ')
        edit_marks_class = input('Введите предмет, по которому необходимо исправить оценки: ')
        print(f'Оценки ученика {edit_marks_student} по предмету {edit_marks_class}: {students_marks[edit_marks_student][edit_marks_class]}')
        ind = int(input('Введите порядковый номер оценки, которую надо изменить: '))-1
        mark = int(input('Введите новую оценку: '))
        students_marks[edit_marks_student][edit_marks_class][ind] = mark
    elif command == 11:
        print('11. Вывести все оценки ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите название предмета: ')
        print(f'Оценки ученика {student} по предмету {class_}: {students_marks[student][class_]}')
    elif command == 12:
        print('12. Вывести все оценки ученика по всем предметам')
        student = input('Введите имя ученика: ')
        print(f'Оценки ученика {student}: ')
        for class_ in classes:
            print(f'\t{class_} - {students_marks[student][class_]}')
    elif command == 13:
        print('13. Вывести средний балл ученика по каждому предмету')
        student = input('Введите имя ученика: ')
        print(f'Средние баллы ученика {student}: ')
        for class_ in classes:
            marks_sum = sum(students_marks[student][class_])
            marks_count = len(students_marks[student][class_])
            print(f'{class_} - {marks_sum//marks_count}')
    elif command == 14:
        print('14. Вывести средний балл ученика по определённому предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите название предмета: ')
        marks_sum = sum(students_marks[student][class_])
        marks_count = len(students_marks[student][class_])
        print(f'Средний балл ученика {student} по предмету {class_}: {marks_sum//marks_count}')
    elif command == 15:
        print('15. Выход из программы')
        break


    
      
      
      
      
      
      
      