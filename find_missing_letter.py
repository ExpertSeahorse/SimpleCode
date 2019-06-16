import string


def find_missing_letter(letters):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    lowercase = []
    uppercase = []
    for letter in lower:
        lowercase.append(letter)
    for letter in upper:
        uppercase.append(letter)
    if letters[0] in lowercase:
        alphabet = lowercase
    else:
        alphabet = uppercase
    starting_index = 0
    for i in range(0, len(alphabet)):
        if letters[0] == alphabet[i]:
            starting_index = i
            break
    k = 0
    for j in range(starting_index, len(alphabet)):
        if not letters[k] == alphabet[j]:
            return alphabet[j]
            break
        k += 1


print(find_missing_letter(['O','Q','R','S']))
