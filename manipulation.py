import main
import keyboard
from client import (response_title, response_author,
                    response_year, response_id, response_search, main_response)
from database import read_json, write_json


def add() -> main:
    book: {str: any} = {
        'id': None,
        'title': response_title(),
        'author': response_author(),
        'year': response_year(),
        'status': True,
    }

    data: dict = read_json()
    if not data:
        data = {
            'count': 0,
            'books': []
        }
    book['id']: int = _auto_id(data)
    data['books'].append(book)
    data['count']: int = data.get('count', 0) + 1
    write_json(data)
    return main.main()


def delete() -> main | str:
    del_id: int = response_id()
    data: dict = read_json()
    if not data['books']:
        print('Файл БД отсутствует или пуст.\n')
        return main.main()
    for book in data['books']:
        if book['id'] == del_id:
            data['books'].remove(book)
            data['count'] = data.get('count', 0) - 1
            break
        else:
            print('Книга с данным ID отсутствует.\n')
            return delete()
    write_json(data)
    return main.main()


def search() -> main:
    field_text: tuple = response_search()
    key_for_search = keyboard.keyboard_search[field_text[0]]
    data = read_json()
    for book in data['books']:
        if field_text[1] in book[key_for_search]:

            for key, value in book.items():
                print(keyboard.keyboard_print[key], value)
            print('-' * 20)
    return main.main()


def show_all():
    pass


def change_status():
    pass


def _auto_id(data) -> int:
    if data['books']:
        max_id: int = data['books'][-1]['id']
        return max_id + 1
    return 1
