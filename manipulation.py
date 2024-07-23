import json

from client import response_title, response_author, response_year
from database import write_json


def add() -> None:
    book = {
        'id': None,
        'title': response_title(),
        'author': response_author(),
        'year': response_year(),
        'status': True,
    }
    write_json(book)



def delete(id):
    pass


def search():
    pass


def show_all():
    pass


def change_status():
    pass
