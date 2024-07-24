from client import (response_title, response_author,
                    response_year, response_id, main_response)
from database import read_json, write_json


def add() -> None:
    book = {
        'id': None,
        'title': response_title(),
        'author': response_author(),
        'year': response_year(),
        'status': True,
    }

    data = read_json()
    if not data:
        data = {
            'count': 0,
            'books': []
        }
    book['id'] = _auto_id(data)
    data['books'].append(book)
    data['count'] = data.get('count', 0) + 1
    write_json(data)


def delete() -> None | str:
    del_id = response_id()
    data = read_json()
    if not data:
        print('Файл БД отсутствует.\n')
        return main_response()
    for book in data['books']:
        if book['id'] == del_id:
            data['books'].remove(book)
            data['count'] = data.get('count', 0) - 1
            break
        else:
            print('Книга с данным ID отсутствует.\n')
            return main_response()
    write_json(data)


def search():
    pass


def show_all():
    pass


def change_status():
    pass


def _auto_id(data) -> int:
    if data['books']:
        max_id = data['books'][-1]['id']
        return max_id + 1
    return 1
