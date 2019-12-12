# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # O(kN)
    def mergeKLists(self, lists: List[ListNode]):
        if len(lists)==1:
            return lists[0]
        if len(lists)==0:
            return None 
        curlists = lists
        while len(curlists)>1:
            curlists = self.mergDivideandConquer(curlists)
        
        return curlists[0]
    
    def mergDivideandConquer(self,lists):
        out = []
        for i in range(0,len(lists)-1,2):
            out.append(self.merger2Lists(lists[i],lists[i+1]))
        if len(lists) % 2 == 1:
            out.append(lists[-1])
        return out
    
    def merger2Lists(self,list1,list2):
        if list1 == None and list2 == None:
            return None
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        outNode = point = ListNode(0)
        while list1 != None and list2 != None:
            if list1.val > list2.val:
                point.next = list2
                list2 = list2.next
            else:
                point.next = list1
                list1 = list1.next
            point = point.next
            
            
        while list1 != None:
            point.next = list1
            point = point.next
            list1 = list1.next
    
        while list2 != None:
            point.next = list2
            point = point.next
            list2 = list2.next
            
        return outNode.next
    
    