import sys
sys.path.insert(0, '/home/anton/HackBulgaria/week01')
from firstDay import to_digits
from secondDay import group


def is_number_balanced(number):
    digits = to_digits(number)
    if (len(digits) % 2 == 0):
        return (sum(digits[0: len(digits) // 2]) ==
                sum(digits[len(digits) // 2:]))
    return (sum(digits[0: len(digits) // 2]) ==
            sum(digits[len(digits) // 2 + 1:]))


# print(is_number_balanced(1238033))
# print(is_number_balanced(4518))
# print(is_number_balanced(9))
# print(is_number_balanced(28471))
# print(is_number_balanced(1238033))


def increasing_or_decreasing(seq):
    is_up = True
    is_down = True
    for i in range(0, len(seq) - 1):
        if seq[i] >= seq[i + 1]:
            is_up = False
        if seq[i] <= seq[i + 1]:
            is_down = False
    if is_up:
        return "Up!"
    if is_down:
        return "Down!"
    return False


# print(increasing_or_decreasing([1, 2, 3, 4, 5]))
# print(increasing_or_decreasing([5, 6, -10]))
# print(increasing_or_decreasing([1, 1, 1, 1]))
# print(increasing_or_decreasing([9, 8, 7, 6]))


def get_largest_palindrome(n):
    for i in reversed(range(0, n)):
        if str(i) == str(i)[::-1]:
            return i
    return 0


# print(get_largest_palindrome(99))
# print(get_largest_palindrome(252))
# print(get_largest_palindrome(994687))
# print(get_largest_palindrome(754649))


def sum_of_numbers(input_string):
    result = 0
    curr_number = ""
    for x in input_string:
        if x.isdigit():
            curr_number += x
        else:
            if curr_number != "":
                result += int(curr_number)
                curr_number = ""
    if curr_number != "":
        result += int(curr_number)
    return result


# print(sum_of_numbers("ab125cd3"))
# print(sum_of_numbers("ab12"))
# print(sum_of_numbers("ab"))
# print(sum_of_numbers("1101"))
# print(sum_of_numbers("1111O"))
# print(sum_of_numbers("1abc33xyz22"))
# print(sum_of_numbers("0hfabnek"))


def birthday_ranges(birthdays, ranges):
    return [(sum([i >= x[0] and i <= x[1] for i in birthdays]))
            for x in ranges]


# print(birthday_ranges([1, 2, 3, 4, 5],
#                       [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))
# print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15],
#                       [(4, 9), (6, 7), (200, 225), (300, 365)]))


digit_to_letters = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz"
}

CAPITALIZE = 1
SPACE = 0
END_SEQUENCE = -1


def numbers_to_message(pressed_sequence):
    message = ""
    grouped_sequence = group(pressed_sequence)
    to_capital = False
    for x in grouped_sequence:
        if x == [1]:
            to_capital = True
        elif x == [0]:
            message += " "
        elif x == [-1]:
            continue
        else:
            letter = digit_to_letters[x[0]][(len(x) - 1) %
                                            len(digit_to_letters[x[0]])]
            if to_capital:
                message += letter.upper()
            else:
                message += letter
            to_capital = False
    return message


# print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]))
# print(numbers_to_message([2, 2, 2, 2]))
# print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3,
#                           3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))


def letter_to_numbers(letter):
    for button, letters in digit_to_letters.items():
        if letter in letters:
            return [button] * (letters.index(letter) + 1)


def message_to_numbers(message):
    numbers = []
    prev = -1
    for x in message:
        if x == " ":
            numbers.append(0)
        else:
            numbers_list = letter_to_numbers(x.lower())
            if x.isupper():
                numbers.append(1)
            elif prev == numbers_list[0]:
                numbers.append(-1)
            numbers.extend(numbers_list)
            prev = numbers_list[0]
    return numbers


# print(message_to_numbers("abc"))
# print(message_to_numbers("a"))
# print(message_to_numbers("Ivo e Panda"))
# print(message_to_numbers("aabbcc"))


def elevator_trips(people_weight, people_floors, elevator_floors,
                   max_people, max_weight):
    trips_count = 0
    people_in_elevator, weight_in_elevator = 0, 0
    floors_visited = set()

    for person in people_weight[:len(people_floors)]:
        if (person + weight_in_elevator > max_weight or
           people_in_elevator + 1 > max_people):
            trips_count += len(floors_visited) + 1
            people_in_elevator, weight_in_elevator = 0, 0
            floors_visited = set()
        floors_visited.add(people_floors[people_weight.index(person)])
        people_in_elevator += 1
        weight_in_elevator += person

    if len(floors_visited) != 0:
        trips_count += len(floors_visited) + 1
    return trips_count


# print(elevator_trips([], [], 5, 2, 200))
# print(elevator_trips([40, 50], [], 5, 2, 200))
# print(elevator_trips([40, 40, 100, 80, 60], [2, 3, 3, 2, 3], 3, 5, 200))
# print(elevator_trips([80, 60, 40], [2, 3, 5], 5, 2, 200))

def char_histogram(string):
    dictionary = {}
    for x in string:
        if x in dictionary:
            dictionary[x] += 1
        else:
            dictionary[x] = 1
    return dictionary


def anagrams():
    words = input().split(' ')
    first_word = char_histogram(words[0].lower())
    second_word = char_histogram(words[1].lower())
    if first_word == second_word:
        return "ANAGRAMS"
    return "NOT ANAGRAMS"


# print(anagrams())


def helper(idx, digit):
    if idx % 2 == 1:
        if (2 * int(digit) > 10):
            return 2 * int(digit) - 9
        return 2 * int(digit)
    return int(digit)


def is_credit_card_valid(number):
    return sum([helper(idx, digit)
               for idx, digit in enumerate(str(number)[::-1])]) % 10 == 0


print(is_credit_card_valid(79927398713))
print(is_credit_card_valid(79927398715))


def is_prime(n):
    return n > 1 and all([n % i for i in range(2, n)])


def goldbach(n):
    return [(x, n - x) for x in range(2, n // 2 + 1)
            if is_prime(x) and is_prime(n - x)]


print(goldbach(4))
print(goldbach(6))
print(goldbach(8))
print(goldbach(10))
print(goldbach(100))


def bombed_position(m, x, y, curr_x, curr_y):
    if (x >= 0 and y >= 0 and x < len(m) and y < len(m[x])):
        m[x][y] = max(m[x][y] - m[curr_x][curr_y], 0)


def bomb_position_and_sum(matrix, x, y):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (-1, -1), (1, -1), (-1, 1)]
    m = [list(row) for row in matrix]
    for x1, y1 in directions:
        bombed_position(m, x + x1, y + y1, x, y)
    return sum(map(sum, m))


def matrix_bombing_plan(m):
    dict_matrix = {}
    for row in range(len(m)):
        for col in range(len(m[row])):
            dict_matrix[(row, col)] = bomb_position_and_sum(m, row, col)
    return dict_matrix


# print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


STAY_IN_THE_SAME = '.'
GO_BACK = '..'
UNNECESSERY = ''


def reduce_file_path(path):
    directs = path.split("/")
    reduced_path = []
    for direc in directs:
        if direc == UNNECESSERY or direc == STAY_IN_THE_SAME:
            continue
        elif direc == GO_BACK:
            if reduced_path != []:
                reduced_path.pop()
        else:
            reduced_path += ['/' + direc]
    if reduced_path == []:
        return "/"
    return "".join(reduced_path)


# print(reduce_file_path("/"))
# print(reduce_file_path("/srv/../"))
# print(reduce_file_path("/srv/www/htdocs/wtf/"))
# print(reduce_file_path("/srv/www/htdocs/wtf"))
# print(reduce_file_path("/srv/./././././"))
# print(reduce_file_path("/etc//wtf/"))
# print(reduce_file_path("/etc/../etc/../etc/../"))
# print(reduce_file_path("//////////////"))
# print(reduce_file_path("/../"))
