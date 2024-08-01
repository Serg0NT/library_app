import keyboard
from client import main_menu
from database import read_json


def main(data: dict) -> None:
    answer = main_menu()
    try:
        keyboard.keyboard_main[answer](data)
    except KeyError:
        print('Такой команды не существует\n')
    finally:
        main(data)


if __name__ == '__main__':
    data: dict = read_json()
    main(data)
