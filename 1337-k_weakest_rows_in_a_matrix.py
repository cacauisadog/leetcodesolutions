# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/


def k_weakest_rows(mat: list[list[int]], k: int) -> list[int]:
    hash_map = {}

    for i, row in enumerate(mat):
        hash_map[i] = row.count(1)

    sorted_map = sorted(hash_map.items(), key=lambda i: i[1])

    answer = []
    i = 0
    while i < k:
        answer.append(sorted_map[i][0])
        i += 1

    return answer
