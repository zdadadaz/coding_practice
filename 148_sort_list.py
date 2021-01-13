# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # TLE
    def sortList_top_bottom(self, head: ListNode) -> ListNode:
        if head==None or head.next ==None : return head
        
        slow = head
        fast = head.next
        while fast and fast.next :
            fast = fast.next.next
            slow = head.next
        mid = slow.next
        slow.next = None
        return self.mergeList(self.sortList(head), self.sortList(mid))
    
    def mergeList(self, l1, l2):
        head = ListNode(0)
        tail = head
        
        while l1 and l2 :
            if l1.val > l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next
        
        if l1: tail.next = l1
        if l2: tail.next = l2
        
        return head.next
            
        