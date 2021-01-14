# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head

            prev.next = tmp

            prev = prev.next.next
            head = head.next

        return root.next
