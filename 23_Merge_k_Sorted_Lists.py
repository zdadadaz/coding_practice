# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        l = 0
        r = len(lists)-1
        out = self.merge_sort(l, r, lists)
        return out
        
    def merge_sort(self, l, r, lists):
        if l >= r :
            return lists[l]
        mid = (l+r)//2
        out_l = self.merge_sort(l,mid,lists)
        out_r = self.merge_sort(mid+1,r,lists)
        return self.merge(out_l, out_r)
        
    def merge(self, link_l, link_r):
        cur = dummy = ListNode()
        while link_l or link_r:
            node = None
            if link_l and link_r:
                if link_l.val < link_r.val:
                    node = link_l
                    link_l = link_l.next
                    node.next = None
                else:
                    node = link_r
                    link_r = link_r.next
                    node.next = None
            else:
                node = link_l if link_l else node
                node = link_r if link_r else node
                link_l = link_l.next if link_l else None
                link_r = link_r.next if link_r else None
                node.next = None
            cur.next = node
            cur = cur.next
        return dummy.next
        
            