def is_isogram(string):
    letters = set()
    for char in string.lower():
        if char in letters and char.isalpha():
            return False
        else:
            letters.add(char)
    return True
