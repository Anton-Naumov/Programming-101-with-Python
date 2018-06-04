def sum_of_digits(n):
    if n < 0:
        n *= -1

    sum = 0

    while n > 0:
        sum += n % 10

        n //= 10

    return sum

#print(sum_of_digits(225))


def to_digits(n):
    digits = []
    if n < 0:
        n = -n

    while n > 0:
        digits = [n % 10] + digits
        n //= 10

    return digits


#print(to_digits(-12345))


def to_number(digits):
    return "".join(map(str, digits))


#print(to_number([1, 2, 3]))


def fact(n):
    result = 1
    for x in range(2, n + 1):
        result *= x
    return result


# print(fact(5))


def fact_digits(n):
    sum = 0
    for x in to_digits(n):
        sum += fact(x)
    return sum


# print(fact_digits(999))


def fib(n):
    first = 1
    second = 1
    while n > 0:
        save = first
        first = second
        second = save + second
        n -= 1
    return first


def fibonacci(n):
    return [fib(x) for x in range(n)]


# print(fibonacci(10))


def fib_number(n):
    return "".join(map(str, fibonacci(n)))


# def fib_number(n):
#   return "".join([str(i) for i in fibonacci(n)])


# print(fib_number(10))


def palindrome(n):
    strN = str(n)
    if len(strN) % 2 == 0:
        return strN[0: len(strN) // 2] == strN[len(strN) // 2:][::-1]
    return strN[0: len(strN) // 2] == strN[len(strN) // 2 + 1:][::-1]


# print(palindrome(123))
# print(palindrome(1221))
# print(palindrome(12321))


def isVowel(letter):
    if letter in "aeiouy":
        return 1
    return 0


def count_vowels(str):
    return sum([isVowel(i) for i in str])


# print(count_vowels("Python"))
# print(count_vowels("Theistareykjarbunga"))


def char_histogram(string):
    dictionary = {}
    for x in string:
        if x in dictionary:
            dictionary[x] += 1
        else:
            dictionary[x] = 1
    return dictionary


# print(char_histogram("Python!"))
# print(char_histogram("AAAAaaa!!!"))
