# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        prv = None
        def lenlist(ll):
            n = 0
            cur = ll
            while cur:
                n+=1
                cur = cur.next
            return n
        
        def ll_walk(ll, step):
            while ll and step>0:
                ll = ll.next
                step -= 1
            return ll
                
        nA = lenlist(headA)
        nB = lenlist(headB)
        curlong = headA
        curshort = headB
        if nA < nB:
            curlong = headB
            curshort = headA
        d = abs(nA-nB)
        curlong = ll_walk(curlong, d)
        while curlong and curshort:
            if curlong == curshort:
                return curlong
            curlong = ll_walk(curlong, 1)
            curshort = ll_walk(curshort, 1)
        return None

