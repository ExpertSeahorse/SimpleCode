def narcissistic(value):
    str_num = str(value)
    len_num = len(str_num)
    answer = 0
    for i in range(len_num):
        answer += int(str_num[i]) ** len_num

    if answer == value:
        return True
    else:
        return False


print(narcissistic(4887))
