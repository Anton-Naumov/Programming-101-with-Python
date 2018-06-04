def validate_fraction(fraction):
    if type(fraction) is not tuple:
        raise ValueError("The argument is not a tuple!")
    if (len(fraction) != 2 or type(fraction[0]) is not int or
       type(fraction[1]) is not int):
        raise ValueError("The argument is not a valid tuple!")
    if fraction[1] == 0:
        raise ZeroDivisionError("Devision by zero!")


def simplify_fraction(fraction):
    validate_fraction(fraction)

    chasno = min(fraction[0], fraction[1])
    remainder = max(fraction[0], fraction[1]) % min(fraction[0], fraction[1])
    while remainder != 0:
        chasno, remainder = remainder, chasno % remainder
    return (fraction[0] // chasno, fraction[1] // chasno)


def collect_fractions(fractions):
    if type(fractions) is not list:
        raise ValueError("The argument is not a list!")
    for fraction in fractions:
        validate_fraction(fraction)

    result = (0, 1)
    for next_frac in fractions:
        result = (result[0] * next_frac[1] + next_frac[0] * result[1],
                  result[1] * next_frac[1])
        result = simplify_fraction(result)
    return result


def sort_fractions(fractions):
    if type(fractions) is not list:
        raise ValueError("The argument is not a list!")
    for fraction in fractions:
        validate_fraction(fraction)

    for i in range(0, len(fractions) - 1):
        for j in range(i, len(fractions)):
            if (fractions[i][0] * fractions[j][1] > fractions[j][0] *
               fractions[i][1]):
                fractions[i], fractions[j] = fractions[j], fractions[i]
    return fractions
