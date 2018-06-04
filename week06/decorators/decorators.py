from functools import wraps


def accepts(*args_types):
    def accepter(func):
        @wraps(func)
        def decorated(*args):
            for pos, arg_type in enumerate(args_types):
                if type(args[pos]) is not arg_type:
                    raise TypeError('Argument {} of {} is not {}'.format(pos,
                                                                         func.__name__,
                                                                         arg_type.__name__))
            return func(*args)
        return decorated
    return accepter


@accepts(str, str, int)
def say_hello(name, last_name, age):
    return "Hello, I am {} {} and I am {} years old".format(name, last_name, age)


def encrypt(shift):
    def accepter(func):
        @wraps(func)
        def decorated(*args):
            string = func(*args)
            return shift_func(string, shift)
        return decorated
    return accepter


def shift_func(string, shift):
    result_string = []
    for c in string:
        if c.isalpha():
            is_capital = c == c.upper()
            shifted_letter = chr(((ord(c.lower()) + shift) - ord('a')) % 26 + ord('a'))

            if is_capital:
                shifted_letter = shifted_letter.upper()

            result_string.append(shifted_letter)
        else:
            result_string.append(c)

    return ''.join(result_string)


@encrypt(2)
def get_low():
    return "Get get get low"


def log(file_name):
    def accepter(func):
        @wraps(func)
        def decorated(*args):
            from datetime import datetime
            with open(file_name, 'a') as f:
                start_time = datetime.now()
                result = func(*args)
                f.write(f'{func.__name__} was called at {str(start_time)}\n')
            return result
        return decorated
    return accepter


@log('log.txt')
@encrypt(2)
def get_lower():
    return "Get get get low"


def performance(file_name):
    def accepter(func):
        @wraps(func)
        def decorated(*args):
            import time
            with open(file_name, 'a') as f:
                start_time = time.time()
                result = func(*args)
                duration = time.time() - start_time
                f.write(f'{func.__name__} was called and took {duration:.02} seconds to complete\n')
            return result
        return decorated
    return accepter


@performance('log.txt')
def something_heavy():
    from time import sleep
    sleep(2)
    return "I am done!"


def main():
    print(say_hello('Anton', 'Naumov', 20))
    # print(say_hello('Anton', 'Naumov', 'str'))

    # print(get_low())

    print(get_lower())

    print(something_heavy())


if __name__ == '__main__':
    main()
