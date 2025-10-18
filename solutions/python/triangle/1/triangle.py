def equilateral(sides):
    a, b, c = sides
    if (a + b < c or b + c < a or a + c < b) or a + b + c == 0:
        return False
    return a == b == c


def isosceles(sides):
    a, b, c = sides
    if (a + b < c or b + c < a or a + c < b) or a + b + c == 0:
        return False
    return a == b or b == c or c == a


def scalene(sides):
    a, b, c = sides
    if (a + b < c or b + c < a or a + c < b) or a + b + c == 0:
        return False
    return a != b and b != c and c != a
