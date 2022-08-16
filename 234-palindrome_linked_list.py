# https://leetcode.com/problems/palindrome-linked-list/

def is_palindrome(head):
    complete_list = []
    while head:
        complete_list.append(head.val)
        head = head.next

    len_complete_list = len(complete_list)

    if len_complete_list == 1:
        return True

    half_of_list = int(len_complete_list/2)
    first_half = complete_list[0:half_of_list]

    if len_complete_list % 2 == 0:
        second_half = complete_list[half_of_list::1]

    else:
        second_half = complete_list[(half_of_list)+1::1]

    return first_half == second_half[::-1]

