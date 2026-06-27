def is_armstrong_number(number):
    armstrong_number = 0
    power = len(str(number))

    for digit in str(number):
        armstrong_number += int(digit) ** power

    return armstrong_number == number
