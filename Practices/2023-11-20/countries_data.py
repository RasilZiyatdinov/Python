import json

with open('countries-data.json', 'r') as f:
    countries = json.load(f)

# Сортировка по названию
sorted_by_name = sorted(countries, key=lambda x: x['name'])
print([country['name'] for country in sorted_by_name])

# Сортировка по столице
sorted_by_capital = sorted(countries, key=lambda x: x['capital'])
print('\n')
print([country['capital'] for country in sorted_by_capital ])

# Сортировка по численности населения
sorted_by_population = sorted(countries, key=lambda x: x['population'], reverse=True)
print('\n')
print('\n'.join([f"{country['name']} {country['population']}" for country in sorted_by_population]))

# Наиболее распространенные языки
from collections import Counter

languages = Counter(language for country in countries for language in country['languages'])
most_common_languages = languages.most_common(10)
print("\n")
print('\n'.join([f"{language} {count}" for language, count in most_common_languages]))

# Наиболее населенные страны
most_populated_countries = sorted(countries, key=lambda x: x['population'], reverse=True)[:10]
print('\n')
print('\n'.join([f"{country['name']} {country['population']}" for country in most_populated_countries]))