# https://leetcode.com/problems/palindrome-number/


def is_palindrome(x: int) -> bool:
    str_number = str(x)
    return str_number == str_number[::-1]


def is_palindrome_without_str(x: int) -> bool:
    reverse_x = 0
    tmp_x = x

    while tmp_x > 0:
        last_digit = tmp_x % 10
        reverse_x = (reverse_x * 10) + last_digit
        tmp_x = tmp_x // 10

    return x == reverse_x
