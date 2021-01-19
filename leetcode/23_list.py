from typing import List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        tmp = []
        for list in lists:
            while list:
                tmp.append(list.val)
                list = list.next

        tmp.sort()
        root = head = ListNode(0)

        # 다시 연결리스트
        for n in tmp:
            head.next = ListNode(n)
            head = head.next

        return root.next
