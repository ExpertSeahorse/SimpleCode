def base_converter(num, old_base, new_base):
    """
    Converts a number of any base into another base
    :param num:
    :param old_base:
    :param new_base:
    :return:
    """
    def hex_convert(arr):
        import string
        # Builds a dictionary like: {A: 0}
        hex_table = {index: letter for index, letter in enumerate(string.ascii_uppercase, start=10)}
        arr_num = []
        for digit in arr:
            try:
                int(digit)
            except ValueError:
                digit.capitalize()

            if digit in hex_table:
                digit = hex_table[int(digit)]

            elif digit in hex_table.values():
                digit = list(hex_table.keys())[list(hex_table.values()).index(digit)]

            arr_num.append(digit)

        return arr_num
    num = str(num)
    # Converts the number into base 10 if not already
    if old_base != 10:
        # Generates a list of digits for the number
        arr_num = []
        for digit in num:
            try:
                arr_num.append(int(digit))
            except ValueError:
                arr_num.append(digit.capitalize())

        # If hex, converts letters into numbers
        if old_base == 16:
            arr_num = hex_convert(arr_num)

        # Finds the radix point in the number
        try:
            radix = arr_num.index('.')
        except ValueError:
            radix = len(arr_num)

        # Uses the digits to move the number from old_base to base 10
        base10 = 0
        for pos in range(len(arr_num)):
            # Determines the weight of the digit based on its position relative to the radix
            if pos < radix:
                weight = -(pos - radix + 1)
            elif pos == radix:
                continue
            else:
                weight = -(pos - radix)

            # Adds (digit * base^weight) to the running total
            base10 += arr_num[pos] * (old_base**weight)

        base10 = str(base10)

    else:
        base10 = num

    # converts the base 10 intermediary into new_base if n_b isn't 10
    if new_base != 10:
        # Finds the decimal place if there is one
        try:
            new_radix = base10.index('.')
        except ValueError:
            new_radix = len(base10)

        # Grabs the whole number part of base10
        base10int = float(base10[0: new_radix])

        # Grabs the fractional part of the base10, if there is one
        try:
            base10frac = float(base10[new_radix:])
        except ValueError:
            base10frac = 0

        # converts whole number from base 10 to new_base
        int_digits = []
        while base10int:
            int_digits.append(int(base10int % new_base))
            base10int = int(base10int / new_base)

        # converts fractional from base 10 to new_base
        frac_digits = []
        while base10frac:
            a = base10frac * new_base
            frac_digits.append(int(a))
            base10frac = a - int(a)

        # converts the whole number remainders into chars
        new_arr = list(map(str, int_digits[::-1]))

        # adds the fractional remainders if they exist
        if frac_digits:
            new_arr += ['.'] + list(map(str, frac_digits))

        # If moving
        if new_base > 10:
            new_arr = hex_convert(new_arr)

        return "".join(new_arr)

    else:
        return base10


num1 = input("Enter the first number: ")
base1 = int(input("Enter its base: "))
num2 = input("Enter the second number: ")
base2 = int(input("Enter its base: "))
sign = input("Enter the sign of the operation you want to do (+,-,*,/): ")

num1_10 = int(base_converter(num1, base1, 10))
num2_10 = int(base_converter(num2, base2, 10))
if sign == '+':
    ans = num1_10 + num2_10
elif sign == '-':
    ans = num1_10 - num2_10
elif sign == '*':
    ans = num1_10 * num2_10
elif sign == '/':
    ans = num1_10 / num2_10


print("Base 10:", ans)
print("Base", str(base1) + ":", base_converter(ans, 10, base1))
if base1 != base2:
    print("Base", str(base2) + ":", base_converter(ans, 10, base2))
input()
