from manipulation import add, delete, search, show_all, change_status

# словарь нужен для ассоциации введеных символов с запускаемыми фукциями
keyboard_main: {str: str} = {
    'д': add,
    'у': delete,
    'п': search,
    'в': show_all,
    'с': change_status,
}

# словарь нужен для ассоциации введеных символов с полями для поиска книги
keyboard_search: {str: str} = {
    'н': 'title',
    'а': 'author',
    'г': 'year',
}


