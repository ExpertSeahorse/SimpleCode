def tribonacci(signature, n):
    answer = []
    if n == 0:
        return answer
    p = signature.pop()
    q = signature.pop()
    r = signature.pop()

    print(p, q, r)
    if n == 1:
        answer.append(r)
    elif n == 2:
        answer.append(r)
        answer.append(q)
    elif n == 3:
        answer.append(r)
        answer.append(q)
        answer.append(p)
    else:
        answer.append(r)
        answer.append(q)
        answer.append(p)
        for i in range(0, n-3):

            s = p + q + r
            answer.append(s)
            r = q
            q = p
            p = s
    return answer


def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3):
        res.append(sum(res[-3:]))
    return res


print(tribonacci([3, 2, 1], 10))