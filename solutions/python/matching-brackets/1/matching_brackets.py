def is_paired(input_string):
    stack = []

    bracket_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    openers = set(bracket_map.values())

    for char in input_string:
        if char in openers:
            stack.append(char)

        elif char in bracket_map:

            if not stack:
                return False

            last_opener = stack.pop()

            if last_opener != bracket_map[char]:
                return False

    return len(stack) == 0