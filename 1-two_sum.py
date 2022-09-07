# https://leetcode.com/problems/two-sum/


def o2_two_sum(nums: list[int], target: int) -> list[int]:
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums):
            if i == j:
                continue

            if num1 + num2 == target:
                return [i, j]


def two_sum(nums: list[int], target: int) -> list[int]:
    visited_map = {}

    for i, num in enumerate(nums):
        remaining = target - num
        position = visited_map.get(remaining)
        if position is not None and position != i:
            return [position, i]

        visited_map[num] = i


def test_o2():
    nums = [2, 7, 11, 15]
    target = 9
    expected_result = [0, 1]
    result = o2_two_sum(nums, target)
    assert result == expected_result

    nums = [3, 2, 4]
    target = 6
    expected_result = [1, 2]
    result = o2_two_sum(nums, target)
    assert result == expected_result

    nums = [3, 3]
    target = 6
    expected_result = [0, 1]
    result = o2_two_sum(nums, target)
    assert result == expected_result


def test():
    nums = [2, 7, 11, 15]
    target = 9
    expected_result = [0, 1]
    result = two_sum(nums, target)
    assert result == expected_result

    nums = [3, 2, 4]
    target = 6
    expected_result = [1, 2]
    result = two_sum(nums, target)
    assert result == expected_result

    nums = [3, 3]
    target = 6
    expected_result = [0, 1]
    result = two_sum(nums, target)
    assert result == expected_result


test_o2()
test()
