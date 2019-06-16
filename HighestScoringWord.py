def high(x):
    solution_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,
    }
    totals_dict = {}
    xlist = x.split(" ")
    print(xlist)
    for index, i in enumerate(xlist):
        total = 0
        for char in i:
            total += solution_dict[char]
        totals_dict[i] = total
    print(totals_dict)

    value_answer = 0
    for key in totals_dict:
        value = totals_dict[key]
        if value > value_answer:
            value_answer = value
            key_answer = key
    return key_answer


def higher(x):
    s, n = x.split(), [sum(ord(c) - 96 for c in y) for y in x.split()]
    print(n)
    return s[n.index(max(n))]


print(higher('take me to semynak'))