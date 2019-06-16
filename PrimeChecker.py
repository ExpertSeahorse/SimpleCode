def prime(nums):
    if nums == 0 or nums == 1:
        return 0
    b = 0
    c = 0
    x = 3
    primes = [2]

    while x <= nums:
        for i in primes:
            if x % i == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
            b += 1
            if b == 1000 and num >= 1000000:
                c += 1
                print(c, ". Found 1000")
                b = 0
    print(len(primes))
    return primes


num = 1000000
print(prime(num))
