def count_substrings(haystack, needle):
    counter = 0
    x = 0
    while x <= len(haystack) - len(needle):
        if haystack[x: x + len(needle)] == needle:
            counter += 1
            x += len(needle)
        else:
            x += 1
    return counter


# print("count_substrings tests:")
# print(count_substrings("This is a test string", "is"))
# print(count_substrings("babababa", "baba"))
# print(count_substrings("Python is an awesome language to program in!", "o"))
# print(count_substrings("We have nothing in common!", "really?"))
# print(count_substrings("This is this and that is this", "this"))


def sum_matrix(m):
    # return sum(map(sum, m))
    return sum([sum(line) for line in m])


# print("sum_matrix tests:")
# print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
# print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))


def nan_expand(times):
    if (times == 0):
        return ""
    return "".join(["Not a " for x in range(0, times)]) + "NaN"


# print("nan_expand tests:")
# print(nan_expand(0))
# print(nan_expand(1))
# print(nan_expand(2))
# print(nan_expand(3))


def is_prime(n):
    return sum([(n % i == 0) for i in range(2, n)]) == 0


def prime_factorization(n):
    resultList = []
    for x in range(2, n + 1):
        if is_prime(x):
            bestPower = 0
            for y in range(1, n):
                if (n % (x ** y) == 0):
                    bestPower = y
            if bestPower != 0:
                resultList.append((x, bestPower))
                n //= (x ** bestPower)
        if (n == 1):
            return resultList


# print("prime_factorization tests:")
# print(prime_factorization(10))
# print(prime_factorization(14))
# print(prime_factorization(356))
# print(prime_factorization(89))
# print(prime_factorization(1000))


def my_group(l):
    resultList = []
    currIdx = 0
    while (currIdx < len(l)):
        nextList = [l[currIdx]]
        currIdx += 1
        while currIdx < len(l) and l[currIdx] == nextList[0]:
            nextList.append(l[currIdx])
            currIdx += 1
        resultList.append(nextList)
    return resultList


def group(arr):
    result = []
    current_group = [arr[0]]
    for item in arr[1:]:
        if item == current_group[0]:
            current_group.append(item)
        else:
            result.append(current_group)
            current_group = [item]
    result.append(current_group)
    return result


# print("group tests:")
# print(group([1, 1, 1, 2, 3, 1, 1]))
# print(group([1, 2, 1, 2, 3, 3]))


def max_consecutive(items):
    return max([len(subS) for subS in group(items)])


# print("max_consecutive tests:")
# print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
# print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))


def check_dir(matrix, x, y, dirX, dirY, currWord, word):
    if (x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0])):
        return False
    currWord += matrix[x][y]
    if (currWord == word):
        return True
    return check_dir(matrix, x + dirX, y + dirY, dirX, dirY, currWord, word)


def count_words(matrix, word):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (-1, -1), (1, -1), (-1, 1)]
    counter = 0
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[x])):
            for x1, y1 in directions:
                counter += check_dir(matrix, x, y, x1, y1, "", word)
    if (word == word[::-1]):
        return counter // 2
    return counter


def take_matrix_input():
    word = input()
    sizeOfMatrix = input().split(" ")
    rows = int(sizeOfMatrix[0])
    matrix = []
    for x in range(0, rows):
        matrix.append(input().split(" "))
    print(count_words(matrix, word))


# take_matrix_input()


def gas_stations(distance, tank_size, stations):
    stations_visited = []
    fuel = tank_size - stations[0]
    stations.append(distance)
    for x in range(0, len(stations) - 1, 1):
        distance_to_next_station = stations[x + 1] - stations[x]
        # if distance_to_next_station > tank_size:
        #     print("It is not possible to travel the distance!")
        #     return
        if distance_to_next_station > fuel:
            stations_visited.append(stations[x])
            fuel = tank_size
        fuel -= distance_to_next_station
    return stations_visited


# print("gas_stations tests:")
# print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
# print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))

# print("Printing test %.5d on day %.2f." % (1, 2))
