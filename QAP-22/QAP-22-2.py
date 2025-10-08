order_ids = 0

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty")
            return None
        
    def __len__(self):
        return len(self.queue)
    
    def find_order(self, order):
        if order in self.queue:
            return self.queue.index(order)
        else: return None

    def find_order_by_id(self, order_id):
        ids_list = list(map(lambda x: x.id, self.queue))
        if order_id in ids_list: 
            return  ids_list.index(order_id)
        else: 
            print("No such order in queue")
            return None

    def is_in_queue(self, order):
        return order in self.queue
        

class Order:
    def __init__(self, customer_name, dishes, prio=0) -> None:
        self.customer_name = customer_name
        self.dishes = dishes
        self.status = 'new'
        self.prio = prio
        global order_ids
        self.id = order_ids
        order_ids += 1

    def __str__(self) -> str:
        return f'Order ID: {self.id}; customer name: {self.customer_name}; dishes: {self.dishes}; priority: {self.prio}; status: {self.status}'
        

class RestaurantQueue:
    def __init__(self) -> None:
        self.queue = Queue()

    def is_empty(self): #Проверяет, пуста ли очередь.
        return self.queue.is_empty
    
    def add_order(self, order): #Добавляет новый заказ в очередь.
        self.queue.enqueue(order)

    def take_order(self): #Извлекает и возвращает первый заказ из очереди.
        taken = self.queue.dequeue()
        taken.status = 'in progress'
        return taken

    def complete_order(self, order): #Отмечает заказ как выполненный.
        order.status = 'complete'
        if self.queue.is_in_queue(order):
            ind = self.queue.find_order(order)
            self.queue.queue.remove(self.queue.queue[ind])

    def print_queue(self): #Выводит информацию о текущих заказах в очереди.
        for i in range(len(self.queue)):
            print(f'{i+1}. {self.queue.queue[i]}')

    def cancel_order(self, order_id): #Отменяет заказ по его идентификатору. Потребуется модификация класса Order и реализация поиска по очереди.
        ind = self.queue.find_order_by_id(order_id)
        if isinstance(ind, int): self.queue.queue.remove(self.queue.queue[ind])
        else: print('There is no such order in queue')

    def modify_order(self, order_id, new_dishes): #Изменяет список блюд в заказе по его идентификатору.
        ind = self.queue.find_order_by_id(order_id)
        if isinstance(ind, int): self.queue.queue[ind].dishes = new_dishes
        else: print('There is no such order in queue')

    def set_priority(self, order_id, priority): #Устанавливает приоритет заказа по его идентификатору.
        ind = self.queue.find_order_by_id(order_id)
        if isinstance(ind, int): self.queue.queue[ind].prio = priority
        else: print('There is no such order in queue')

best_kitchen_orders = RestaurantQueue()
best_kitchen_orders.add_order(Order('Pete', ['fish', 'chips']))
best_kitchen_orders.print_queue()
best_kitchen_orders.add_order(Order('Jane', ['steak', 'mashed potatoes']))
best_kitchen_orders.add_order(Order('Richard', ['fish', 'chips', 'beer']))
best_kitchen_orders.add_order(Order('Nina', ['fish', 'chips', 'lemon fresh']))
best_kitchen_orders.add_order(Order('Sam', ['cheeseburger', 'beer']))
best_kitchen_orders.add_order(Order('Ann', ['apple tart', 'strawberry milkshake', 'banana ice-cream']))
best_kitchen_orders.add_order(Order('Mike', ['steak', 'veggies salad']))
best_kitchen_orders.print_queue()
print(best_kitchen_orders.take_order())
best_kitchen_orders.print_queue()
x = 7
print(f'Queue number of order with id = {x} is {best_kitchen_orders.queue.find_order_by_id(x)}')
best_kitchen_orders.complete_order(Order('Mike', ['steak', 'veggies salad']))
best_kitchen_orders.add_order(Order('Victor', ['veggies salad']))
best_kitchen_orders.print_queue()
best_kitchen_orders.cancel_order(2)
best_kitchen_orders.print_queue()
best_kitchen_orders.cancel_order(9)
best_kitchen_orders.modify_order(4, ['mac-n-cheese', 'Cherry Ale'])
best_kitchen_orders.set_priority(4,1)
best_kitchen_orders.print_queue()