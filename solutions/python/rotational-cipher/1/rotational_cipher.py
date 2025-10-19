def rotate(text, key):
    for index, char in enumerate(text):
        if char.isalpha():
            ascii_value = ord(char.upper()) + key
            if ascii_value > 90:
                ascii_value -= 26

            if char.islower():
                ascii_value += 32

            text = text[:index] + chr(ascii_value) + text[index + 1:]
    return text