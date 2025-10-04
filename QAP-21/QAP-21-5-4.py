class Person:
    def __init__(self, name=None, age=None, gender=None, occupation=None):
       self.name = name
       self.age = age
       self.gender = gender
       self.occupation = occupation
    def set_attributes(self, attr_dict):
        for k, v in attr_dict.items():
            if k == 'name': self.name = v
            elif k == 'age': self.age = v
            elif k == 'gender': self.gender = v
            elif k == 'occupation': self.occupation = v
    def show_card(self):
        print('Name: {0}\nAge: {1}\nGender: {2}\nOccupation: {3}'.format(self.name, self.age, self.gender, self.occupation))

p1 = Person()
p1.set_attributes({'name': 'Elon', 'age': 51, 'gender': 'Male', 'occupation': 'CEO', 'company': 'Tesla'})
p1.show_card()
# Name: Elon
# Age: 51
# Gender: Male
# Occupation: CEO
p2 = Person(name='Mark', occupation='Expert')
p2.set_attributes({'name': 'Bob', 'occupation': 'Worker', 'company': 'StenWoods'})
p2.show_card()
# Name: Bob
# Age: None
# Gender: None
# Occupation: Worker

