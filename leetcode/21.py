# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = []
        list2 = []

        while l1.next:
            list1.append(l1.val)
            l1 = l1.next

        list1.append(l1.val)

        while l2.next:
            list1.append(l2.val)
            l2 = l2.next

        list2.append(l2.val)

        merge_list = sorted(list1 + list2)

        result: ListNode = ListNode(self, merge_list[0], None)

        for i in range(1, len(merge_list)):
            result.next = val = merge_list[i]
            result = result.next

        return result
