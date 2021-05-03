# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.res = []
        self.dfs(nestedList)
        # print(self.res)
        
    def next(self) -> int:
        return self.res.pop(0)
    
    def hasNext(self) -> bool:
        if not self.res:
            return False
        return True
        
    def dfs(self, nest):
        if not nest:
            return
        # print(nest,self.res)
        for i in nest:
            if i.isInteger():
                self.res.append(i.getInteger())   
            else:
                self.dfs(i.getList())

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())