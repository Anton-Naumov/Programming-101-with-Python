from view import View
from models import initialize_database


if __name__ == '__main__':
    initialize_database()
    View().start()
