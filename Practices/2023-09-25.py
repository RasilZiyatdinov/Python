import random

print("Task1")
list1 = [random.randint(0, 100) for _ in range(10)]
print("Исходный список:", list1)
list1.reverse()
print("Перевернутый список:", list1)

print("\nTask2")
list1 = [random.randint(0, 100) for _ in range(10)]
list2 = [random.randint(0, 100) for _ in range(10)]
print("Первый список:", list1)
print("Второй список:", list2)
list3 = []
for i in range(len(list1)):
    if i % 2 == 0:
        list3.append(list1[i])
for i in range(len(list2)):
    if i % 2 == 1:
        list3.append(list2[i])
print("Третий список:", list3)

print("\nTask3")
list1 = [random.choice([1, 2, 3, "a", "b", "c", 4.5, 6.7]) for _ in range(10)]
print("Исходный список:", list1)
list1 = list(set(list1))
print("Список без дубликатов:", list1)

print("\nTask4")
dict = {f"key_{i}": random.choice([47, 9.8, 123, 5]) for i in range(10)}
print("Исходный словарь:", dict)
uniqs = list(set(dict.values()))
result = []
for val in uniqs:
    keys = [key for key in dict if dict[key] == val]
    result.append((val, keys))
print("Результат:", result)

print("\nTask5")
dict1 = {f"key_{i}": random.randint(0, 5) for i in range(5)}
dict2 = {f"key_{i}": random.randint(0, 5) for i in range(5)}
print("Первый словарь:", dict1)
print("Второй словарь:", dict2)
intersection = set(dict1.values()) & set(dict2.values())
result = {}
for key, val in dict1.items():
    if val in intersection:
        result.update({key: val})
for key, val in dict2.items():
    if val in intersection:
        result.update({key: val})
print("Результат:", result)