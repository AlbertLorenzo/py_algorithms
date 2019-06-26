def get_letter_count(vector, condition):
    n_letters = 0
    for x in vector:
        if x == condition:
            n_letters += 1
    return n_letters

def xo(str):
    vector = list(str.lower())
    x = get_letter_count(vector, 'x')
    o = get_letter_count(vector, 'o')
    return x == o

# def xoCount(str):
#     s = str.lower()
#     return s.count('x') == s.count('o')

print(xo("xo"))