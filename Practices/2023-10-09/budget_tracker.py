import json

def save_to_file(budget_tracker):
    with open('budget_tracker.json', 'w', encoding="utf-8") as f:
        json.dump(budget_tracker, f, ensure_ascii=False, indent=4)

def load_from_file():
    try:
        with open('budget_tracker.json', 'r', encoding="utf-8") as f:
            budget_tracker = json.load(f)    
    except FileNotFoundError:
        budget_tracker = {'actions': {}, 'limits': {}}
    return budget_tracker

def add_operation(description, amount, category):
    budget_tracker = load_from_file()
    if category not in budget_tracker['actions']:
        budget_tracker['actions'][category] = []
    budget_tracker['actions'][category].append({"description": description, "amount": amount})
    save_to_file(budget_tracker)

def set_limit(category, limit):
    budget_tracker = load_from_file()
    budget_tracker['limits'][category] = limit
    save_to_file(budget_tracker)

def check_limit(category):
    budget_tracker = load_from_file()
    actions = budget_tracker['actions'][category]
    total_expenses = sum([abs(action["amount"]) for action in actions if action["amount"] < 0])
    limit =  budget_tracker['limits'][category]
    if total_expenses > limit:
        print(f"Вы превысили лимит расходов по категории {category}")
    else:
        print(f"Вы не превысили лимит расходов по категории {category}")

def analise_category(category):
    result = {'expenses': 0, 'incomes': 0}
    budget_tracker = load_from_file()
    actions = budget_tracker['actions'][category]
    for action in actions:
            if action['amount'] < 0:
                result['expenses'] += action['amount']
            else:
                result['incomes'] += action['amount']
    return result


if __name__ == '__main__':
    budget_tracker = load_from_file()

    while True:
        print("\nМеню")
        print("1. Добавить операцию")
        print("2. Аналитика по категории")
        print("3. Установить лимит на категорию")
        print("4. Проверить лимит по категории")
        print("5. Выход")

        action = input(">> ")

        if action == '1':
            description = input("Введите описание операции: ")
            amount = float(input("Введите сумму (доход sum, расход -sum): "))
            category = input("Введите категорию: ")
            add_operation(description, amount, category)
        elif action == '2':
            category = input("Введите категорию: ")
            result = analise_category(category)
            print(f"Сумма доходов по категории {category}: {result['incomes']}")
            print(f"Сумма расходов по категории {category}: {result['expenses']}")
        elif action == '3':
            category = input("Введите категорию: ")
            limit = float(input("Введите сумму лимита: "))
            set_limit(category, limit)
        elif action == '4':
            category = input("Введите категорию: ")
            check_limit(category)
        elif action == '5':
            break
        else:
            print("Неверный ввод")


