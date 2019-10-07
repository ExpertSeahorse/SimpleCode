class RomanNumerals:
    @staticmethod
    def to_roman(num):
        conversion_dict = (('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50),
                           ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1))
        answer = []
        for (key, value) in conversion_dict:
            while num >= value:
                answer.append(key)
                num -= value
        return "".join(answer)

    @staticmethod
    def from_roman(roman):
        conversion_dict = (('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50),
                           ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1))
        answer = 0
        for (key, value) in conversion_dict:
            answer += value * roman.count(key)
            roman.replace(key, "")
        return answer


h = RomanNumerals.to_roman(1107)
print(h)
print(RomanNumerals.from_roman(h))
