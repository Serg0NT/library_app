import json


def read_json():
    return json.load(open('data.json'))


def write_json(book):
    try:
        data = read_json()
    except FileNotFoundError:
        print('Файл отсутствует')
        data = {
            'count': 0,
            'books': []
        }
    book['id'] = _auto_id(data)

    data['books'].append(book)
    data['count'] = data.get('count', 0) + 1
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=2)


def _auto_id(data) -> int:
    if data['books']:
        max_id = data['books'][-1]['id']
        print(max_id)
        return max_id + 1
    else:
        return 1
