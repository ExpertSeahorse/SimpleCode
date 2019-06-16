def find_outlier(integers):
    tag1 = False
    tag2 = False
    for i in range(len(integers)):
        if i == 0:
            tag1 = integers[0] % 2 == 0
        elif i == 1:
            tag2 = integers[1] % 2 == 0

        elif tag1 == tag2:
            tagx = integers[i] % 2 == 0
            if tagx != tag1:
                return integers[i]
        elif tag1 != tag2:
            tagx = integers[2] % 2 == 0
            if tag1 == tagx:
                return integers[1]
            else:
                return integers[0]


def find_outlier(int):
    odds = [x for x in int if x % 2 != 0]
    evens = [x for x in int if x % 2 == 0]
    return odds[0] if len(odds) < len(evens) else evens[0]


print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
