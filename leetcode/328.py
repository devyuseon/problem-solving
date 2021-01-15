# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        cur = head
        root1 = odd = ListNode(0)
        root2 = even = ListNode(0)

        is_odd = True
        while cur:
            if is_odd:
                tmp = ListNode(cur.val)
                odd.next = tmp
                odd = odd.next
            else:
                tmp = ListNode(cur.val)
                even.next = tmp
                even = even.next
            cur = cur.next
            is_odd = not is_odd

        # merge
        odd.next = root2.next

        return root1.next
