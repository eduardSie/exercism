def is_pangram(sentence):
    pangram = set("thequickbrownfoxjumpsoverthelazydog")
    return pangram.issubset(set(sentence.lower()))