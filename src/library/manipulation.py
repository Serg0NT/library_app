import main
import keyboard
from client import (response_title, response_author,
                    response_year, response_id, response_search, response_status)
from database import write_json
from lexicon import lexicon_status, lexicon_print


def add(data: dict) -> None:
    """
    Добавляет новую книгу.
    """
    book: {str: any} = {
        'id': None,
        'title': response_title(),
        'author': response_author(),
        'year': response_year(),
        'status': True,
    }
    if not data:
        data = {
            'count': 0,
            'books': []
        }
    book['id']: int = _auto_id(data)
    data['books'].append(book)
    data['count']: int = data.get('count', 0) + 1
    write_json(data)


def delete(data: dict) -> None:
    """
    Удаляет книгу по введеному id
    """
    _check_empty_data(data)

    del_id: int = response_id()
    del_book = _find_curr_book(del_id, data)
    if del_book:
        data['books'].remove(del_book)
        data['count'] = data.get('count', 0) - 1
    else:
        print('Книга с данным ID отсутствует.\n')
        return delete(data)
    write_json(data)


def search(data: dict) -> main:
    """
    Ищет книгу по введенному параметру
    (автор, название или год)
    """
    _check_empty_data(data)

    field_text: tuple = response_search()
    key_for_search = keyboard.keyboard_search[field_text[0]]
    for book in data['books']:
        if field_text[1] in book[key_for_search]:
            for key, value in book.items():
                if key == 'status':
                    value = lexicon_status[value]
                print(lexicon_print[key], value)
            print('-' * 20)
    main.main(data)


def show_all(data: dict) -> main:
    """
    Выводит список всех книг.
    """
    _check_empty_data(data)

    for book in data['books']:
        for key, value in book.items():
            if key == 'status':
                value = lexicon_status[value]
            print(lexicon_print[key], value)
        print('-' * 20)

    main.main(data)


def change_status(data: dict):
    """
    Меняет статус книги
    """
    _check_empty_data(data)
    curr_id = response_id()
    curr_book = _find_curr_book(curr_id, data)
    if not curr_book:
        print('Книга с данным ID отсутствует.\n')
        return change_status(data)
    ind = data['books'].index(curr_book)
    status = response_status()
    if status not in ['в наличии', 'выдана']:
        print('Такой статус не существует')
        return change_status(data)
    if status == 'в наличии':
        curr_book['status'] = True
    else:
        curr_book['status'] = False

    data['books'][ind] = curr_book
    write_json(data)


def _auto_id(data: dict) -> int:
    """
    Генерирует автоматическое значение id
    """
    if data['books']:
        max_id: int = data['books'][-1]['id']
        return max_id + 1
    return 1


def _find_curr_book(curr_id: int, data: dict) -> dict | None:
    """
    Ищет книгу в БД по введенному id
    """
    for book in data['books']:
        if book['id'] == curr_id:
            return book


def _check_empty_data(data: dict):
    if not data or not data['books']:
        print('Файл БД отсутствует или пуст.\n')
        return main.main(data)
