def is_isogram(word):
    return len(word) == len(set(word.lower()))

def is_isogram_loop(word):
    lowered_word = word.lower()
    check = True
    for char in lowered_word:
        if char.count(char) > 1:
            check = False
    return check 

print(is_isogram("albert"))