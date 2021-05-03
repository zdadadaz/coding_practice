# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        length = 0
        while cur:
            length+= 1
            cur = cur.next
        idx = length - n
        dummy = ListNode()
        dummy.next = head
        cur = dummy.next
        prv = dummy
        cnt = 0 
        while cur:
            tmp = cur.next
            if idx == cnt:
                prv.next = tmp
                break
            prv = cur
            cur = tmp
            cnt+=1
        return dummy.next
            

    def removeNthFromEnd_nfast(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        fast = cur = dummy
        for i in range(n+1):
            fast = fast.next

        while fast:
            fast = fast.next
            cur = cur.next
        
        cur.next = cur.next.next
        return dummy.next
            