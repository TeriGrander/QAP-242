phonebook = {}
stop = 'y'
while stop.lower() != 'n':
    name = input('Enter name: ')
    number = input('Enter phone number: ')
    phonebook[name] = number
    stop = input('Enter next? y/n: ')
print(f'All contacts: {phonebook.keys()}')
print(f'All numbers: {phonebook.values()}')
print('whole phonebook:')
for name, number in phonebook.items():
    print(f'Name: {name} phone: {number}')
new = int(input('How many new records? '))
names = []
numbers = []
for i in range(new):
    names.append(input('Enter new name '))
    numbers.append(input('Enter their number '))
for i in range(new):
    phonebook[names[i]] = numbers[i]
print('whole phonebook:')
for name, number in phonebook.items():
    print(f'Name: {name} phone: {number}')
ed = input('what name to edit number for? ')
new_num = input('enter new number: ')
phonebook[ed] = new_num
find = input('who to look for? ')
if find in phonebook.keys(): print(f"{find}'s number is {phonebook[find]}")
else: print('no such name in phonebook')
rem = input('what name to remove? ')
del phonebook[rem]
print('whole phonebook:')
for name, number in phonebook.items():
    print(f'Name: {name} phone: {number}')