import json
json_data = '''

{
    "glossary": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": [
                            "GML",
                            "XML"
                        ]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    }
}
'''
# Функция для получения значения по ключу из JSON-данных
def get_value_by_key(json_data, key):
    parsed_json = json.loads(json_data)
    try:
        value = parsed_json[key]
        return value
    except KeyError:
        return f"key '{key}' not found in JSON data"

# Запрашиваем у пользователя ключ
key_to_find = input("Enter the name of the key to get the corresponding value from JSON: ")

# Получаем значение по ключу и выводим его
result = get_value_by_key(json_data, key_to_find)
print(result)