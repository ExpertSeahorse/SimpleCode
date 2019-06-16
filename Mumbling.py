def accum(s):
    answer = []
    for i, letter in enumerate(s,1):
        q = letter * i
        answer.append(q.capitalize())
    return '-'.join(answer)


print(accum('abcd'))
