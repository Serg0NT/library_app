from manipulation import add, delete, search, show_all, change_status

keyboard_main: {str: str} = {
    'д': add,
    'у': delete,
    'п': search,
    'в': show_all,
    'с': change_status,
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
