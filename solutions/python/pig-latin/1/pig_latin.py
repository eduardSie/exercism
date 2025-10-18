def translate(text):
    def translate_word(word):
        vowels = 'aeiou'

        if not word:
            return ""

        if word[0] in vowels or word.startswith(('xr', 'yt')):
            return word + 'ay'

        split_index = 0
        for i, letter in enumerate(word):

            if letter == 'y' and i > 0:
                split_index = i
                break

            if letter in vowels:
                split_index = i

                if letter == 'u' and i > 0 and word[i - 1] == 'q':
                    split_index += 1

                break

        consonants = word[:split_index]
        rest_of_word = word[split_index:]

        return rest_of_word + consonants + "ay"


    words = text.split(' ')

    translated_words = [translate_word(word) for word in words]

    return ' '.join(translated_words)

