# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head

        # find middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse
        rev = None
        while slow:
            tmp = slow.next
            slow.next = rev
            rev = slow
            slow = tmp

        # check palindrome
        left, right = head, rev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
