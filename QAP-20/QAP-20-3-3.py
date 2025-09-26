import os, json

data = {
'translator' :
    {
    'bugs':'ошибка', 
    'function':'функция', 
    'approve':'согласовать'
    }, 
1:'int key', 
'set':(0, 1, 2, 3),
'empty value':None
}

path = r'F:\PlayProgrammerСurrent\QAP-242\QAP-20'
file = 'data.json'
full_path = os.path.join(path, file)

with open(full_path, 'w') as f:
    json.dump(data, f)

with open(full_path, 'r') as f:
    read_data = json.load(f)

print(data)
print(read_data)