# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        import random
        self.head = head
        tmp = head
        self.nodelen = 0
        while tmp.next:
            self.nodelen += 1
            tmp = tmp.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        rand = random.randint(0,self.nodelen)
        tmp = self.head
        while rand>0:
            rand -= 1
            tmp = tmp.next
        return tmp.val
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()