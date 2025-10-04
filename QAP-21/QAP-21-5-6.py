class Queue:
    def __init__(self) -> None:
        self.items = []
    
    def enqueue(self, number):
        self.items.append(number)

    def dequeue(self):
        self.items.pop(0)

    def is_empty(self):
        return not self.items
    
    def show_queue(self):
        for i in self.items:
            print(i, end=' ')
        print('')


# Создаём объект класса Queue
q = Queue()

# Добавляем элементы в очередь
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Выводим элементы очереди
q.show_queue()  

# 1 2 3

# Удаляем элементы из очереди
q.dequeue()
q.dequeue()

# Выводим элементы очереди
q.show_queue()  

# 3
