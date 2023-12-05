import json

with open('countries.json', 'r') as f:
    countries = json.load(f)

# прописные названия стран с помощью map()
upper_countries = list(map(lambda x: x.upper(), countries))
print(upper_countries)

# страны, содержащие 'land', с помощью filter()
land_countries = list(filter(lambda x: 'land' in x, countries))
print(land_countries)

# страны, содержащие ровно 6 символов, с помощью filter()
six_char_countries = list(filter(lambda x: len(x) == 6, countries))
print(six_char_countries)

# страны, содержащие 6 и более символов, с помощью filter()
six_or_more_char_countries = list(filter(lambda x: len(x) >= 6, countries))
print(six_or_more_char_countries)

# страны, не начинающиеся с символа 'E', с помощью filter()
not_e_start_countries = list(filter(lambda x: x[0] != 'E', countries))
print(not_e_start_countries)

# С помощью `reduce()` объедините все страны и получите данное предложение на английском языке: 
# Финляндия, Швеция, Дания, Норвегия и Исландия являются странами Северной Европы
from functools import reduce
north_europe = ['Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
north_europe_sentence = reduce(lambda x, y: x + ', ' + y, north_europe) + ' are countries of Northern Europe'
print(north_europe_sentence)

# объединение: прописные страны не начинающиеся с символа 'E' и имеющие ровно 6 символов
six_char_and_not_e_countries = list(filter(lambda x: len(x) == 6, map(lambda x: x.upper(), filter(lambda x: x[0] != 'E', countries))))
print(six_char_and_not_e_countries)

# Функция `categorize_countries()`, 
# которая возвращает список стран с некоторым общим шаблоном (например, `'land', 'ia', 'island', 'stan'`), который можно менять
def categorize_countries(pattern):
    return lambda countries: list(filter(lambda x: pattern in x, countries))

land_countries = categorize_countries('land')(countries)
print(land_countries)

ia_countries = categorize_countries('ia')(countries)
print(ia_countries)

island_countries = categorize_countries('Island')(countries)
print(island_countries)

stan_countries = categorize_countries('stan')(countries)
print(stan_countries)
