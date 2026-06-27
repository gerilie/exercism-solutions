def equilateral(sides):
    if not is_triangle(sides):
        return False

    a = sides[0]
    b = sides[1]
    c = sides[2]

    return a == b == c


def isosceles(sides):
    if not is_triangle(sides):
        return False

    a = sides[0]
    b = sides[1]
    c = sides[2]

    return a == b or a == c or b == c


def scalene(sides):
    if not is_triangle(sides):
        return False

    a = sides[0]
    b = sides[1]
    c = sides[2]

    return a != b != c and a != c


def is_triangle(sides):
    if len(sides) != 3:
        raise ValueError("The triangle must have 3 sides")

    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a == 0 or b == 0 or c == 0:
        return False

    is_a_b_greater_c = a + b >= c
    is_b_c_greater_a = b + c >= a
    is_a_c_greater_b = a + c >= b

    return is_a_b_greater_c and is_b_c_greater_a and is_a_c_greater_b
