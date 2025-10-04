class Group:
    members = []

class Student:
    course = 'Data Science'
    
s1 = Student()
setattr(s1, 'name', 'Иван')
setattr(s1, 'surname', 'Иванов')
setattr(s1, 'semester', 1)

s2 = Student()
setattr(s2, 'name', 'Лев')
setattr(s2, 'surname', 'Сергеев')
setattr(s2, 'semester', 1)

Group.members.extend([s1, s2])

result = Group.members
