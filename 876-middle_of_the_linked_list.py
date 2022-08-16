# https://leetcode.com/problems/middle-of-the-linked-list/


def middle_node(head):
    aux = []
    while head:
        aux.append(head)
        head = head.next

    return aux[int(len(aux) / 2)]
