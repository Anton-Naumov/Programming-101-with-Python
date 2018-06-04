import sqlite3
from settings import DB_NAME


def data_base(data_base_name, read_only=False, db_parameter=False):
    def accepter(func):
        def decorated(cls, *args, **kwargs):
            result = None
            with sqlite3.connect(DB_NAME) as db:
                cursor = db.cursor()

                if db_parameter is True:
                    result = func(cls, db, cursor, *args, **kwargs)
                else:
                    result = func(cls, cursor, *args, **kwargs)

                if not read_only:
                    db.commit()
            return result
        return decorated
    return accepter


def catch_and_print_exception(exception_type):
    def accepter(func):
        def decorated(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_type as e:
                print(str(e))
        return decorated
    return accepter
