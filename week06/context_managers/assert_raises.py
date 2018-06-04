from contextlib import contextmanager


# class assertRaises:
#     def __init__(self, exception, msg=None):
#         self.exception = exception
#         self.msg = msg
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is self.exception and str(exc_val) == self.msg:
#             print('Success!')
#             return True
#         elif exc_type is self.exception:
#             raise Exception('Raised exception message is not the expected!')
#         elif exc_type is None:
#             raise Exception('Exception not raised!')
#         else:
#             raise Exception('Wrong exception raised!')


@contextmanager
def assertRaises(exception, msg=None):
    try:
        yield
        print(f'Exception \"{exception.__name__}\" not raised!')
    except Exception as e:
        if isinstance(e, exception) and str(e) == msg:
            print('Success!')
            return True
        elif isinstance(e, exception):
            print(f'Exception message \"{str(e)}\" is not the expected \"{msg}\"!')
            raise e
        else:
            print(f'Exception raised \"{e.__class__.__name__}\" is not the expected \"{exception.__name__}\"!')
            raise e


if __name__ == '__main__':
    # with assertRaises(ValueError, 'error'):
    #     raise ValueError('error')

    # with assertRaises(ValueError, 'error'):
    #     raise ValueError('wrong message')

    with assertRaises(ValueError, 'error'):
        pass

    # with assertRaises(ValueError, 'error'):
    #     raise Exception('error')
