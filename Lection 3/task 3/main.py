import json
""""
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
"""
with open('data_js.json','r') as file:
    json_data=file.read()
def get_value_by_key(data, key):
    if isinstance(data, dict):
        if key in data:
            return data[key]
        else:
            for k, v in data.items():
                result = get_value_by_key(v, key)
                if result is not None:
                    return result
    elif isinstance(data, list):
        for item in data:
            result = get_value_by_key(item, key)
            if result is not None:
                return result

    return None

key_to_find = input("Enter the name of the key to get the corresponding value from JSON: ")
parsed_json = json.loads(json_data)
result = get_value_by_key(parsed_json, key_to_find)
if result is not None:
    print(result)
else:
    print(f"Key '{key_to_find}' not found in JSON data")