# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return None
        if k == 0:
            return head
        cnt = 0
        cur = head
        while cur.next != None:
            cnt += 1
            cur = cur.next
        cnt += 1
        
        if cnt == 1:
            return head
        
        inverse_idx = cnt - (k%cnt)
        if inverse_idx== cnt:
            return head
        prev = None
        newhead = head
        while inverse_idx >0:
            prev = newhead
            newhead = newhead.next
            inverse_idx -= 1
            
        cur.next = head
        prev.next = None
        
        return newhead