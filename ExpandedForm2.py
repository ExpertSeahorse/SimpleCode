def expanded_form(num):
    parts = list(reversed(str(num)))
    print(parts)
    dot = parts.index(".")
    pos_parts = parts[dot:]
    n1eg_parts = parts[:dot]
    neg_parts = list(reversed(n1eg_parts))
    print(neg_parts)
    rev_exp_num = []
    for i in range(len(neg_parts)-1, -1, -1):
        if neg_parts[i] == "0" or neg_parts[i] == ".":
            continue
        rev_exp_num.append(str(neg_parts[i]) + "/" + str(10 ** (i+1)))

    for i in range(0, len(pos_parts)):
        if pos_parts[i] == "0" or pos_parts[i] == ".":
            continue
        rev_exp_num.append(str((10 ** (i-1)) * int(pos_parts[i])))
    return ' + '.join(list(reversed(rev_exp_num)))


def expanded_form(num):
    integer_part, fractional_part = str(num).split('.')

    result = [str(int(num) * (10 ** i)) for i, num in enumerate(integer_part[::-1]) if num != '0'][::-1]
    result += [str(num) + '/' + str(10 ** (i + 1)) for i, num in enumerate(fractional_part) if num != '0']

    return ' + '.join(result)


print(expanded_form(7.304))

