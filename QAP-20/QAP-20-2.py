import os
import shutil
print(os.getcwd())
print(os.listdir())
cwd = os.getcwd() # 'C:\\Users\\Liudmila\\Python'
new_dir = 'test'
path = os.path.join(cwd, new_dir) # генерируем путь до новой папки
#os.mkdir(path) # создаем новую папку
print(os.listdir())


# file = r'F:\PlayProgrammerСurrent\python.txt'
# os.remove(file)
# copy_file = shutil.copy(file, path)
