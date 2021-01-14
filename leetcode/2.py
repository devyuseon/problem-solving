# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node != None:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    def makeNewList(self, result_int: int) -> ListNode:
        tmp = str(result_int)
        head = ListNode(tmp[0])
        prev = head

        for i in range(1, len(tmp)):
            node = ListNode(tmp[i])
            head.next = node
            head = head.next

        return prev

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # l1,l2 역순으로 뒤집기
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)

        # 하나씩 리스트로 저장
        l1_list = []
        l2_list = []

        while l1:
            l1_list.append(str(l1.val))
            l1 = l1.next
        while l2:
            l2_list.append(str(l2.val))
            l2 = l2.next

        # 리스트를 str로
        l1_str = "".join(l1_list)
        l2_str = "".join(l2_list)

        # 두 수 더하기
        result_int = int(l1_str) + int(l2_str)

        # 거꾸로 연결리스트에 담기
        result_list = self.makeNewList(result_int)
        result_list = self.reverseList(result_list)

        return result_list
