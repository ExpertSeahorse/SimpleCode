from math import gcd


def proper_fractions(n):
    print(n)
    ans = 0
    for i in range(1, n, 2):
        if gcd(i, n) == 1:
            print(i)
            ans += 1
    return ans


print(proper_fractions(5))
