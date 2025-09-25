def assign_tasks_to_engineers(names, tasks):
    return list(zip(names, tasks))


engineers = ["Анна", "Иван", "Елена", "Олег"]
tasks = ["Тестирование UI", "Тестирование API", "Написание тестовых сценариев"]

pairs = assign_tasks_to_engineers(engineers, tasks)
print(pairs)
# [('Анна', 'Тестирование UI'), ('Иван', 'Тестирование API'), ('Елена', 'Написание тестовых сценариев')]