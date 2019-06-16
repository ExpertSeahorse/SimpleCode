def order_weight(strng):
    weight_list = strng.split(" ")
    weight_tuple_list = []
    answer_list = []

    for entry in weight_list:
        weight_sum = 0
        for digit in entry:
            weight_sum += int(digit)
        tuple_pair = (entry, weight_sum)
        weight_tuple_list.append(tuple_pair)

    max_value = 0
    for entry in weight_tuple_list:
        if entry[1] > max_value:
            max_value = entry[1]

    for answer_entry in range(0, len(weight_tuple_list)):
        m_v = max_value + 1
        for tuple_entry in weight_tuple_list:
            if tuple_entry[1] <= m_v:
                m_v = tuple_entry[1]
                name = tuple_entry[0]

        answer_list.append(name)
        weight_tuple_list.remove((name, m_v))
    return ' '.join(answer_list)


print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))
