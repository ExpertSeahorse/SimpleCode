def move_zeros(array):
    zero_count = 0
    new_array = []
    for entry in array:
        if str(entry) == 'False':
            new_array.append(entry)
        elif entry != 0:
            new_array.append(entry)
        else:
            zero_count += 1

    for j in range(0,zero_count):
        new_array.append(0)
    return new_array


def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)


print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
