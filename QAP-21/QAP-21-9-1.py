class Student:
    def __init__(self, fio, group):
        self.fio = fio  # ФИО студента (строка)
        self.group = group  # группа (строка)
        self.lect_marks = []  # оценки за лекции
        self.homework_marks = []  # оценки за домашние задания

    def add_lect_marks(self, mark):
        self.lect_marks.append(mark)

    def add_homework_marks(self, mark):
        self.homework_marks.append(mark)

    def __str__(self):
        return f"Студент {self.fio}: оценки на лекциях: {str(self.lect_marks)}; оценки за д/з: {str(self.homework_marks)}"

class Mentor():
    def __init__(self, fio, subject):
        self.fio = fio
        self.subject = subject

    def set_mark(self, student, mark):
        raise NotImplementedError

class Lector(Mentor):
    def __init__(self, fio, subject):
        super().__init__(fio, subject)

    def set_mark(self, student, mark):
        student.add_lect_marks(mark)

    def __str__(self):
        return f'Лектор {self.fio}: предмет {self.subject}'

class Reviewer(Mentor):
    def __init__(self, fio, subject):
        super().__init__(fio, subject)

    def set_mark(self, student, mark):
        student.add_homework_marks(mark)

    def __str__(self):
        return f'Эксперт {self.fio}: предмет {self.subject}'
    
# Проверяем взаимодействие классов Lector, Reviewer и Student
lector = Lector("Gusenko D.", "Physics")
reviewer = Reviewer("Golovanod A.", "Management")
student = Student("Zyablikov D.E.", "M3o-118B")
lector.set_mark(student, 4)
reviewer.set_mark(student, 5)
print(lector)
print(reviewer)
print(student)

# Лектор Gusenko D.: предмет Physics
# Эксперт Golovanod A.: предмет Management
# Студент Zyablikov D.E.: оценки на лекциях: [4]; оценки за д/з: [5]

# Проверяем, что класс Mentor абстрактный 
# и нельзя создать объекты этого класса
try:
    mentor = Mentor("Gusenko D.", "Physics")
    mentor.set_mark(student, 4)

except NotImplementedError as e:
    print("Ошибка")

# Ошибка