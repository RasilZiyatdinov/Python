zoo = {
  'жираф': ['Малая панда', 'Грифы, орланы', 'Тапир', 'Красный волк'],
  'манул': ['Медведь-губач', 'Жираф', 'Малая панда', 'Большая панда'],
}

def get_animal_neighbours(animal: str):
    return zoo.get(animal)


animal = input('Введите животное: ')

neighbours = get_animal_neighbours(animal.lower())

if neighbours:
    print("Соседи:", end=' ')
    print(*neighbours, sep=', ')
else:
    print("Животное не обнаружено")