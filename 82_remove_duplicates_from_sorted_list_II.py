# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode()
        cur = dummy
        rep = 0
        while head and head.next:   
            if head.val == head.next.val:
                head = head.next
                rep = 1
            elif rep == 1:# rep ==1 and head.val != head.next.val
                head = head.next
                rep = 0
            else: # rep ==0 and head.val != head.next.val
                cur.next = head
                head = head.next
                cur.next.next = None
                cur = cur.next
        if head and rep==0: 
                cur.next = head
        return dummy.next