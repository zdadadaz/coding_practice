# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        m = [head.val]
        slow = head
        fast = head
        tot = 0
        while slow :
            if not fast.next:
                tot+=1
                break 
            elif not fast.next.next:
                tot += 2
                break
            else:
                tot+=2
            slow = slow.next
            fast = fast.next.next
            m.append(slow.val)                        
        
        if tot%2 ==1:
            m.pop()
        while m:
            if slow.next.val != m[-1]:
                return False
            slow = slow.next
            m.pop()
        return True

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    def isPalindrome_middle_reverse_find(self, head: ListNode) -> bool:
        slow = head
        fast = head
        # find middle point
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse right parts
        prv = None
        while slow:
            tmp = slow.next
            slow.next = prv
            prv= slow
            slow = tmp
        
        # compare from left and right pointer
        left = head
        right = prv
        while left:
            if right.val != left.val:
                return False
            right = right.next
            left = left.next
        return True