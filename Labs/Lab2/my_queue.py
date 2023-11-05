class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return not bool(self.items)


if __name__ == "__main__":
    queue = Queue()

    while True:
        print("\nМеню")
        print("1. Добавить элемент")
        print("2. Удалить элемент")
        print("3. Просмотреть первый элемент")
        print("4. Просмотреть длину")
        print("5. Выход")

        action = input(">> ")

        if action == "1":
            item = input("Введите элемент: ")
            queue.enqueue(item)
            print(f"Элемент '{item}' добавлен")
        elif action == "2":
            item = queue.dequeue()
            if (item == None):
                print("Очередь пуста")
            else:
                print(f"Элемент '{item}' удален")
        elif action == "3":
            item = queue.peek()
            if (item == None):
                print("Очередь пуста")
            else:
                print(f"Первый элемент: {item}")
        elif action == "4":
            print(f"Длина очереди: {queue.size()}")
        elif action == "5":
            break
        else:
            print("Некорректный ввод")
