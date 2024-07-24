import keyboard
from client import main_response


def main():
    answer = main_response()
    keyboard.keyboard_main[answer]()


if __name__ == '__main__':
    main()
    # res = main()
    # keyboard[res]()
