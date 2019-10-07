def is_interesting(number, awesome_phrases):
    for j in [0, 1, 2]:
        if j == 0:
            exact = 1
        else:
            exact = 0

        if 100 > number+j:
            continue

        num_str = str(number+j)
        num_arr = list(map(int, list(num_str)))

        if number+j in awesome_phrases:
            return 1 + exact

        # First Test (for 900000)
        if num_arr[0] != 0:
            flag = 0
            for i in num_arr[1:]:
                if i == 0:
                    flag += 1
            if flag == len(num_arr[1:]):
                return 1 + exact

        # Second Test (for 99999)
        rep_flag = 0
        incr_flag = 0
        decr_flag = 0
        for i in range(1, len(num_arr)):
            if num_arr[i] == num_arr[i-1]:
                rep_flag += 1
            if num_arr[i]-1 == num_arr[i-1] or (num_arr[i] == 0 and num_arr[i-1] == 9):
                incr_flag += 1
            if num_arr[i]+1 == num_arr[i-1] or (num_arr[i] == 0 and num_arr[i-1] == 1):
                decr_flag += 1
        if rep_flag == len(num_arr)-1:
            return 1 + exact
        elif incr_flag == len(num_arr)-1:
            return 1 + exact
        elif decr_flag == len(num_arr)-1:
            return 1 + exact

        # Test 5
        pal_flag = 0
        for i in range(len(num_arr)):
            k = len(num_arr) - i-1
            if num_arr[i] == num_arr[k]:
                pal_flag += 1
        if pal_flag == len(num_arr):
            return 1 + exact
    return 0


def is_interesting(number, awesome_phrases=[]):
    """

    :param number:
    :param awesome_phrases:
    :return:
    """
    # tests the next two numbers as well
    for j in [0,1,2]:
        # if number isn't exact, return 1
        if j == 0:
            exact = 1
        else:
            exact = 0
        # Dont go unless number is > 100
        if 100 > number+j:
            continue

        # if number in passed phrases
        if number+j in awesome_phrases:
            return 1 + exact
        # if number is round (1000 or 50000)
        elif set(str(number)[1:]) == set('0'):
            return 1 + exact
        # if number is increasing (12345)
        elif str(number) in '1234567890':
            return 1 + exact
        # if number is decreasing (98765)
        elif str(number) in '9876543210':
            return 1 + exact
        # if number is a palindrome
        elif str(number) == str(number)[::-1]:
            return 1 + exact


print(is_interesting(13331, [100, 256]))
