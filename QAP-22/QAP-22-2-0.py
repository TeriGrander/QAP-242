class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")
            return None

    def is_empty(self):
        return len(self.stack) == 0

def is_balanced(expression):
    stack = Stack()
    brackets_pairs = {')': '(', ']': '[', '}': '{'}

    opening_brackets = list(brackets_pairs.values())  # ['(', '[', '{']
    closing_brackets = list(brackets_pairs.keys())  # [')', ']', '}']

    for char in expression:  # Пункт 1-ый
        if char in opening_brackets:
            stack.push(char)  # Пункт 2-ой
        elif char in closing_brackets:  # 3-ий пункт
            if stack.is_empty():  # Стек может оказаться пустым уже в этом моменте
                return False
            elif brackets_pairs[char] != stack.pop():  # Если не пустой, то забираем верхний элемент, и если он
                # не равен соответствующей открывающей скобке, говорим, что не сбалансирован
                return False

    return stack.is_empty()  # 4-ый пункт

expression1 = "(2 * [3 + 4] - {121 * (10 - 7)})"
expression2 = "(2 / [3 - 7] / {11 * (22 + 7)} + 22 ) - 23)"
expression3 = "((2 / [3 - 7] / {11 * (22 + 7)) + 22 ) - 23"
print("Выражение 1 сбалансировано?", is_balanced(expression1))  # True
print("Выражение 2 сбалансировано?", is_balanced(expression2))  # False
print("Выражение 3 сбалансировано?", is_balanced(expression3))  # False