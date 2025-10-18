def square_root(number):
    if number < 0:
        raise ValueError("Negative values are not supported.")

    if number == 0:
        return 0
    if number == 1:
        return 1

    low = 1
    high = number

    while low <= high:
        mid = (low + high) // 2

        square = mid * mid

        if square == number:
            return mid
        elif square < number:
            low = mid + 1
        else:  # square > number
            high = mid - 1
    return None
