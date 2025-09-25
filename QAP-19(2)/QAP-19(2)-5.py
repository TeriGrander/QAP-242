x = 20

def change_global_var():
	global x
	x = 30

def check_global_local():
	x = 0
	
print(x)  # Вывод: 20
change_global_var()
print(x)  # Вывод: 30
check_global_local()
print(x)

