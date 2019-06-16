def comp(array1, array2):

    if None in (array1, array2) or len(array1) != len(array2):
        return False

    newarray = []
    for entry in array1:
        newarray.append(entry * entry)

    if ' '.join(map(str, sorted(newarray))) == ' '.join(map(str, sorted(array2))):
        return True
    else:
        return False


def comp(a1, a2):
    try:
        return sorted([entry ** 2 for entry in a1]) == sorted(a2)
    except:
        return False


print(comp([2, 2, 3], [4, 9, 9]))