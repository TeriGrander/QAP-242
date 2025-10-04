class Student:
    course = 'Data Science'
    
s1 = Student()
setattr(s1, 'name', 'Иван')
setattr(s1, 'surname', 'Иванов')
setattr(s1, 'semester', 1)

result = s1.__dict__