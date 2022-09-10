# https://leetcode.com/problems/merge-two-sorted-lists/


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        result = "["

        while self:
            result += str(self.val) + ", "
            self = self.next

        result = result[:-2] + "]"
        return result


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        merged_list = []

        while list1:
            merged_list.append(list1)
            list1 = list1.next

        while list2:
            merged_list.append(list2)
            list2 = list2.next

        sorted_merged_list = sorted(merged_list, key=lambda i: i.val)

        try:
            for i, item in enumerate(sorted_merged_list):
                item.next = sorted_merged_list[i + 1]
        except IndexError:
            pass

        try:
            return sorted_merged_list[0]
        except IndexError:
            return ListNode(val='')


list1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4, next=None)))
list2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4, next=None)))

solution = Solution()
print(solution.mergeTwoLists(list1, list2))
print(solution.mergeTwoLists(None, None))
