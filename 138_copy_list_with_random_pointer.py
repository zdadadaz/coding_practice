"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummy = Node(0)
        new_node = dummy
        old_node = head
        while old_node:
            new_node.next = Node(old_node.val, old_node.next, old_node.random)
            tmp = old_node.next
            old_node.next = new_node.next
            old_node = tmp           
            new_node = new_node.next
            
        new_node = dummy.next
        old_node = head
        while new_node:
            new_node.random = new_node.random.next if new_node.random else None
            new_node = new_node.next
        return dummy.next

    def copyRandomList_without_space(self, head: 'Node') -> 'Node':
        cur = head
        while cur:
            new_node = Node(cur.val, cur.next, cur.random)
            tmp = cur.next
            cur.next = new_node
            new_node.next = tmp
            cur = tmp
        
        dummy = Node(0)
        new_node = dummy
        cur = head
        while cur:
            new_node.next = cur.next
            new_node.next.random = cur.next.random.next if cur.next.random else None
            new_node = new_node.next
            cur = cur.next.next
        return dummy.next