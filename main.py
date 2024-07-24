from manipulation import add, delete
from client import main_response

if __name__ == '__main__':
    res = main_response().lower()
    if res == 'д':
        add()
    if res == 'у':
        delete()
