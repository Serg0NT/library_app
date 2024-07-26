import json

import main


def read_json() -> dict | None:
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return


def write_json(data) -> None:
    try:
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=2)
        print('Данные записаны успешно\n')

    except Exception as err:
        print(f'Неожиданная ошибка {err}.\n'
              f'Обратитесь в техподдержку')
    finally:
        main.main(data)

