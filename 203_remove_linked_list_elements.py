# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode()
        cur = dummy.next = head
        prv = dummy
        while cur:
            if cur.val == val:
                prv.next = cur.next
            else:
                prv = cur
            cur = cur.next
        return dummy.next