class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return not bool(self.items)
    
if __name__ == "__main__":
    stack = Stack()

    while True:
        print("\nМеню")
        print("1. Добавить элемент")
        print("2. Удалить элемент")
        print("3. Просмотреть верхний элемент")
        print("4. Просмотреть длину")
        print("5. Выход")

        action = input(">> ")

        if action == "1":
            item = input("Введите элемент: ")
            stack.push(item)
            print(f"Элемент '{item}' добавлен")
        elif action == "2":
            item = stack.pop()
            if (item == None):
                print("Стек пуст")
            else:
                print(f"Элемент '{item}' удален")
        elif action == "3":
            item = stack.peek()
            if (item == None):
                print("Стек пуст")
            else:
                print(f"Первый элемент: {item}")
        elif action == "4":
            print(f"Длина стека: {stack.size()}")
        elif action == "5":
            break
        else:
            print("Некорректный ввод")
