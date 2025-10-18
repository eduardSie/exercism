def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    iterations = 0
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = number * 3 + 1
        iterations += 1
    return iterations
