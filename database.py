import json


def read_json() -> dict | None:
    try:
        return json.load(open('data.json'))
    except FileNotFoundError:
        return


def write_json(data):
    try:
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=2)
    except Exception as err:
        print(f'Неожиданная ошибка {err}.\n'
              f'Обратитесь в техподдержку')


