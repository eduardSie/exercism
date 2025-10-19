def is_valid(isbn):

    iter = 10
    sum = 0
    for digit in isbn:
        if digit == "-":
            continue
        elif digit.isdigit():
            sum += int(digit)*iter
            iter -= 1
        elif digit == "X" and iter == 1:
            sum += 10
            iter -= 1
        else:
            return False

    return sum % 11 == 0 and sum != 0 and iter == 0
