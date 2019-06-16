def expanded_form(num):
    parts = list(reversed(str(num)))
    rev_exp_num = []
    for i in range(len(parts)):
        if parts[i] == "0":
            continue
        rev_exp_num.append(str((10 ** i) * int(parts[i])))
    return ' + '.join(list(reversed(rev_exp_num)))


def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')


print(expanded_form(7030))