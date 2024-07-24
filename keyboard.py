from manipulation import add, delete, search

keyboard_main: {str: str} = {
    'д': add,
    'у': delete,
    'п': search,
}

keyboard_search: {str: str} = {
    'н': 'title',
    'а': 'author',
    'г': 'year',
}

keyboard_print: {str: any} = {
    'id': 'ID - ',
    'title': 'Название - ',
    'author': 'Автор - ',
    'year': 'Год издания - ',
    'status': 'Статус - ',
}
