def is_armstrong_number(number):
    digits = list(map(int, str(number)))
    num = 0
    for digit in digits:
        num += pow(digit, len(digits))
    return num == number
