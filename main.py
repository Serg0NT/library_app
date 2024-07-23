from manipulation import add
from client import main_response

if __name__ == '__main__':
    res = main_response()
    if res.lower() == 'д':
        add()
