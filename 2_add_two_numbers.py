# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        deci = 0
        while l1 and l2:
            val = l1.val + l2.val + deci
            deci = val//10
            cur.next = ListNode(val%10)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        l1 = l2 if l2 else l1
        while deci != 0 or l1:
            l1val = l1.val if l1 else 0
            val = l1val + deci
            deci = val//10
            cur.next = ListNode(val%10)
            cur = cur.next
            l1 = l1.next if l1 else None
        return dummy.next

    def addTwoNumbers_singlewhile(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry!=0:
            l2v = l1v = 0
            l2n = l1n = None
            if l1:
                l1v = l1.val
                l1n = l1.next
                l1 = l1.next
            if l2:
                l2v = l2.val
                l2n = l2.next
                l2 = l2.next
            tot = l1v+ l2v + carry
            carry = tot//10
            cur.next=ListNode(tot%10)
            cur = cur.next
        return dummy.next
            
                