import json

def load_from_file():
    try:
        with open('tasks.json', 'r', encoding="utf-8") as f:
            tasks = json.load(f)    
    except FileNotFoundError:
        tasks = {'tasks': []}
    return tasks

def save_to_file(tasks):
    with open('tasks.json', 'w', encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def add_task(task, category):
    tasks = load_from_file()
    tasks['tasks'].append({'task': task, 'category': category, 'done': False})
    save_to_file(tasks)

def done_task(number):
    index = number - 1
    tasks = load_from_file()
    tasks['tasks'][index]['done'] = True
    save_to_file(tasks)

def search_task(descr):
    tasks = load_from_file()
    return [task for task in tasks['tasks'] if str(descr).lower() in str(task['task']).lower()]

def get_tasks_by_category(category):
    tasks = load_from_file()
    return [task for task in tasks['tasks'] if task['category'] == category]

def print_tasks():
    tasks = load_from_file()
    if (len(tasks['tasks']) == 0):
        print("Задач нет")
    else:
        for i, task in enumerate(tasks['tasks']):
            print(f"{i+1}. Описание - {task['task']}, статус - {'done' if task['done'] else 'not done'}, категория - {task['category']}")

if __name__ == '__main__':
    tasks = load_from_file()
    
    while True:
        print("\nМеню")
        print("1. Добавить задачу")
        print("2. Выполнить задачу")
        print("3. Найти задачи по описанию")
        print("4. Вывести все задачи по категории")
        print("5. Вывести весь список задач")
        print("6. Выход")

        action = input(">> ")

        if action == '1':
            description = input("Введите описание задачи: ")
            category = input("Введите категорию задачи: ")
            add_task(description, category)
        elif action == '2':
            number = int(input("Введите номер задачи: "))
            try:
                done_task(number)
            except IndexError:
                print("Неверный номер задачи")
        elif action == '3':
            query = input("Введите строку для поиска: ")
            found_tasks = search_task(query)
            if found_tasks:
                print("Найденные задачи:")
                for i, task in enumerate(found_tasks):
                    print(f"{i+1}. Описание - {task['task']}, статус - {'done' if task['done'] else 'not done'}, категория - {task['category']}")
            else:
                print("Задачи не найдены")
        elif action == '4':
            category = input("Введите категорию: ")
            category_tasks = get_tasks_by_category(category)
            if category_tasks:
                print(f"Задачи в категории '{category}':")
                for i, task in enumerate(category_tasks):
                    print(f"{i+1}. Описание - {task['task']}, статус - {'done' if task['done'] else 'not done'}, категория - {task['category']}")
            else:
                print(f"Задачи не найдены")
        elif action == '5':
            print_tasks()
        elif action == '6':
            break
        else:
            print("Неверный ввод")