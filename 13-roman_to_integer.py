# https://leetcode.com/problems/roman-to-integer/

symbols = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
}


def roman_to_int(s: str) -> int:
    num = 0
    i = 0

    while i < len(s):
        double_letter = ""
        if i < len(s) - 1:
            double_letter = s[i] + s[i + 1]

        if double_letter in symbols:
            num += symbols[double_letter]
            i += 2
        else:
            num += symbols[s[i]]
            i += 1

    print(num)


roman_to_int("III")
roman_to_int("LVII")
roman_to_int("MCMXCIV")
