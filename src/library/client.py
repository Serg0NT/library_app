from lexicon import lexicon


def main_menu() -> str:
    answer = input(lexicon['req_1']).lower()
    if len(answer) != 1:
        print(lexicon['not_none'])
        return main_menu()
    return answer


def response_id() -> int:
    try:
        answer: int = int(input(lexicon['req_id']))
    except ValueError:
        print('Введены некорректные данные. Ожидается ввод числового значения.\n')
        return response_id()
    else:
        if answer > 0:
            return answer
    return response_id()


def response_title() -> str:
    answer: str = input(lexicon['req_title'])
    if len(answer) < 1:
        print(lexicon['not_none'])
        return response_title()
    return answer


def response_author() -> str:
    answer: str = input(lexicon['req_author'])
    if len(answer) < 1:
        print(lexicon['not_none'])
        return response_author()
    return answer


def response_year() -> int:
    try:
        answer: int = int(input(lexicon['req_year']))
    except ValueError:
        print('Введены некорректные данные. Ожидается ввод числового значения.\n')
        return response_year()
    else:
        if 0 < answer < 2024:
            return answer
        return response_year()


def response_search() -> tuple:
    field: str = input(lexicon['for_search']).lower()
    if len(field) != 1:
        print(lexicon['not_none'])
        return response_search()
    text: str = input('Введите Ваш запрос:\n')
    if not text:
        print(lexicon['not_none'])
        return response_search()
    return field, text


def response_status() -> str:
    status: str = input(lexicon['req_status']).lower()
    if len(status) < 1:
        print(lexicon['not_none'])
        return response_status()
    return status