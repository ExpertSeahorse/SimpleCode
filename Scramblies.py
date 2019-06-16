from collections import Counter
import time


def scramble(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    answer = []
    for letter in s2:
        if letter in s1:
            answer.append(letter)
            s1.remove(letter)
    return answer == s2


def scramblerfaster(s1,s2):
    starttime= time.time()
    # Creates a dictionary of how often each letter is in both of the strings
    Cs1 = Counter(s1)
    Cs2 = Counter(s2)
    # Returns True if all the counters in Cs2(word) are smaller than the counters in Cs1(string)
    ans = all(Cs2[i] <= Cs1[i] for i in Cs2)
    print("It took: {} seconds".format(time.time()-starttime))
    return ans


print(scramblerfaster('katas', 'steak'))
