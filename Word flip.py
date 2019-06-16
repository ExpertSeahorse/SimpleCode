def spin_words(sentence):
    phrase = sentence.split()
    new_phrase = []
    for word in phrase:
        if len(word) >= 5:
            word = word[::-1]
        new_phrase.append(word)
    return ' '.join(new_phrase)


print(spin_words("Hey fellow warriors"))
