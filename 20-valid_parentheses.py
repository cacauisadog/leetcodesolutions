# https://leetcode.com/problems/valid-parentheses/


def is_valid(s):
    parentheses_map = {
        "(": ")",
        "{": "}",
        "[": "]",
    }
    char_stack = []

    for c in s:
        if c in parentheses_map:
            char_stack.append(c)
        else:
            if len(char_stack) == 0:
                return False

            last_char = char_stack.pop()
            if c != parentheses_map.get(last_char):
                return False

    if len(char_stack) > 0:
        return False

    return True


def run_test():
    s = "()"
    assert is_valid(s) is True

    s = "(]"
    assert is_valid(s) is False

    s = "()[]{}"
    assert is_valid(s) is True

    s = "]"
    assert is_valid(s) is False


run_test()
