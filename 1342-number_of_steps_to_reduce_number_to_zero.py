# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/


def number_of_steps(num: int) -> int:
    steps = 0

    while num != 0:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num - 1
        steps += 1

    return steps
