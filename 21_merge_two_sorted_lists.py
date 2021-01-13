# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                tmp = l1.next
                l1.next = None
                l1 = tmp
            else:
                cur.next = l2
                tmp = l2.next
                l2.next = None
                l2 = tmp
            cur= cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next
                
            