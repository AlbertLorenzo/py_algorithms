def duplicate_count(word):
    c = 0
    lowered = word.lower()
    for char in set(lowered):
        if lowered.count(char) > 1:
            c += 1
    return c

print(duplicate_count("indivisibility"))