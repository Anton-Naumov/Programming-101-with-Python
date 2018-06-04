def sum_of_digits(n):
    assert type(n) is int
    return sum([int(digit) for digit in str(abs(n))])


def to_digits(n):
    assert type(n) is int
    return [int(digit) for digit in str(abs(n))]


def to_number(digits):
    assert type(digits) is list
    if digits == []:
        return 0
    return int("".join([str(abs(x)) for x in digits]))


def fact(n):
    assert type(n) is int
    assert n >= 0
    if n == 0:
        return 1
    import functools
    return functools.reduce(lambda x, y: x * y, range(1, abs(n) + 1))


def fact_digits(n):
    assert type(n) is int
    return sum([fact(x) for x in to_digits(abs(n))])


def nth_fibonacci(n):
    assert type(n) is int
    first, second = 1, 1
    for i in range(1, abs(n)):
        first, second = second, first + second
    return first


def fibonacci(n):
    assert type(n) is int
    return [nth_fibonacci(i) for i in range(1, abs(n) + 1)]


def fib_number(n):
    return "".join([str(x) for x in fibonacci(n)])


def palindrome(n):
    return str(n) == str(n)[::-1]


def count_vowels(_str):
    return sum([x.lower() in 'aeiouy' for x in str(_str)])


def count_consonants(_str):
    return sum([x.lower() in 'bcdfghjklmnpqrstvwxz' for x in str(_str)])


def char_histogram(string):
    char_hist_dict = {}
    for char in str(string):
        char_hist_dict[char] = char_hist_dict.get(char, 0) + 1
    return char_hist_dict


print(sum_of_digits(1325132435356))
# 43
print(sum_of_digits(123))
# 6
print(sum_of_digits(6))
# 6
print(sum_of_digits(-10))
# 1

print(to_digits(123))
# [1, 2, 3]
print(to_digits(99999))
# [9, 9, 9, 9, 9]
print(to_digits(123023))
# [1, 2, 3, 0, 2, 3]

print(fact_digits(111))
# 3
print(fact_digits(145))
# 145
print(fact_digits(999))
# 1088640

print(fibonacci(1))
# [1]
print(fibonacci(2))
# [1, 1]
print(fibonacci(3))
# [1, 1, 2]
print(fibonacci(10))
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

print(fib_number(3))
# 112
print(fib_number(10))
# 11235813213455

print(count_vowels("Python"))
# 2
print(count_vowels("Theistareykjarbunga"))
# 8
print(count_vowels("grrrrgh!"))
# 0
print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
# 22
print(count_vowels("A nice day to code!"))
# 8

print(count_consonants("Python"))
# 4
print(count_consonants("Theistareykjarbunga")) #It's a volcano name!
# 11
print(count_consonants("grrrrgh!"))
# 7
print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
# 44
print(count_consonants("A nice day to code!"))
# 6

print(char_histogram("Python!"))
# { 'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1 }
print(char_histogram("AAAAaaa!!!"))
# { 'A': 4, 'a': 3, '!": 3 }
