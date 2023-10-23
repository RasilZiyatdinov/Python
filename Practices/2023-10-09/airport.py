import json
import requests
from bs4 import BeautifulSoup
import translators as ts
from deep_translator import GoogleTranslator

url = "https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:_A"

def load_airports_codes():
    data = {}
    # проход по кодам по алфавиту
    for letter in range(65, 91):
        letter_url = url.replace(":_A", ":_" + chr(letter))
        headers = {'User-Agent': 'Mozilla/5.0'}

        response = requests.get(letter_url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        table = soup.find("table", {"class": "wikitable sortable"})
        rows = table.find_all("tr")

        for row in rows[1:]:
            cells = row.find_all("td")
            if len(cells) > 1:
                code = cells[0].text.strip()
                name = cells[2].text.strip()
                data[code] = name
    
    return data

def get_code_by_airport(data, air_name):
    air_name = ts.translate_text(air_name, from_language='auto', to_language='en')
    for code, name in data.items():
        if str(name).lower() == air_name.lower():
            return code
    return "Airport not found"
                

if __name__ == "__main__":
    data = load_airports_codes()

    with open("airports.json", "w") as f:
        json.dump(data, f, indent=4)

    air_name = 'Аэропорт Анапа'
    code = get_code_by_airport(data, air_name)
    print(f"Airport: {air_name}, Code: {code}")

    air_name = 'Darchula Airport'
    code = get_code_by_airport(data, air_name)
    print(f"Airport: {air_name}, Code: {code}")