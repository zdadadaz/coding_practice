# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small = ListNode()
        large = ListNode()
        cur = head
        smallcur = small
        largecur = large
        while cur:
            next_tmp = cur.next
            if cur.val < x:
                smallcur.next = cur
                smallcur = smallcur.next
            elif cur.val >= x:
                largecur.next = cur
                largecur = largecur.next
            cur.next = None
            cur = next_tmp
        
        smallcur.next = large.next
        return small.next