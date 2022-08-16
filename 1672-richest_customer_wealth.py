# https://leetcode.com/problems/richest-customer-wealth/


def maximum_wealth(accounts: list[list[int]]):
    greatest_wealth = 0
    for a in accounts:
        wealth = sum(a)
        if wealth > greatest_wealth:
            greatest_wealth = wealth

    return greatest_wealth
