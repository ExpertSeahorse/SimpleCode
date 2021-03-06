def parse_int(s):
    """
    Converts from word form to integer form
    Example:  seven hundred eighty-three thousand nine hundred and nineteen -> 783919
    :param s:
    :return:
    """
    # Initializing word -> number conversions
    answer = 0
    num_dict = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
    }
    pos_mult = [
        ["hundred", 100],
        ["thousand", 1000],
        ["million", 1000000]
    ]

    temp_answer = 0
    # For every word in the string...
    for entry in s.lower().replace('-', ' ').split(' '):
        flag = False
        # Compare the word with one of the multiplier words
        for i in pos_mult:
            if entry == i[0]:
                temp_answer *= i[1]
                flag = True
                break
        # Otherwise, match it with one of the addition words
        if not flag:
            for name, num in num_dict.items():
                if name == entry:
                    temp_answer += num
                    break
        # if temp answer > 999, roll it over (otherwise the multiplier loop doesnt work correctly)
        if temp_answer > 999:
            answer += temp_answer
            temp_answer = 0

    return answer + temp_answer


print(parse_int("seven hundred eighty-three thousand nine and hundred and nineteen"))
