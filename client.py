from lexicon import lexicon


def main_response() -> str:
    answer = input(lexicon['req_1'])
    if len(answer) != 1:
        print(lexicon['not_none'])
        main_response()
    return answer


def response_id() -> int:
    try:
        answer = int(input(lexicon['req_id']))
    except ValueError:
        print('Введены некорректные данные. Ожидается ввод числового значения.\n')
        return response_id()
    else:
        if answer > 0:
            return answer
    return response_id()

def response_title() -> str:
    answer = input(lexicon['req_title'])
    if len(answer) < 1:
        print(lexicon['not_none'])
        response_title()
    return answer


def response_author() -> str:
    answer = input(lexicon['req_author'])
    if len(answer) < 1:
        print(lexicon['not_none'])
        response_author()
    return answer


def response_year() -> int:
    try:
        answer = int(input(lexicon['req_year']))
    except ValueError:
        print('Введены некорректные данные. Ожидается ввод числового значения.\n')
        return response_year()
    else:
        if 0 < answer < 2024:
            return answer
        return response_year()
